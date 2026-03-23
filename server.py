"""
Miami Resources — Production Server

Inference stack:
  1. NVIDIA NIM (Nemotron via NemoClaw) — primary
  2. Google ADK / Gemini 2.5 Flash — fallback
"""

import json
import logging
import os
import uuid

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from miami_resources.data.programs import PROGRAMS, format_program, search_programs
from miami_resources.tools.lookup import (
    check_snap_eligibility,
    get_crisis_resources,
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("miami-resources")

app = FastAPI(title="Miami Resources", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Config ───────────────────────────────────────────────────
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")
NVIDIA_MODEL = "nvidia/nemotron-3-super-120b-a12b"
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")

# ── System prompt ────────────────────────────────────────────
SYSTEM_PROMPT = """You are **Miami Resources** — a free, multilingual assistant that helps Miami-Dade County residents find housing, food, healthcare, jobs, and education programs.

LANGUAGE: Detect the user's language and respond in the same language. Support English, Spanish, and Haitian Creole.

BEHAVIOR:
- Be warm, patient, non-judgmental
- Ask 1-2 clarifying questions to find the best match
- Always provide phone numbers, websites, and addresses so people can take action
- Keep responses concise and scannable (mobile users)
- For emergencies: 911. For any need: dial 211 (305-358-4357, 24/7, multilingual)
- Crisis: Suicide 988, DV Hotline 1-800-799-7233, Homeless 1-877-994-4357

You have access to these verified Miami-Dade programs:

{programs}

When answering:
1. Match the user's need to the most relevant programs
2. Include the program name, what it does, eligibility, phone, and website
3. If someone is in crisis, give emergency numbers FIRST
4. If you don't know something, say so and recommend calling 211"""


def _build_system_prompt(language: str = "en") -> str:
    """Build system prompt with compact program listing."""
    lines = []
    for cat in ["housing", "food", "healthcare", "jobs", "education", "general"]:
        progs = search_programs(category=cat)
        if progs:
            lines.append(f"\n## {cat.upper()}")
            for p in progs:
                lang = language if language in ("en", "es", "ht") else "en"
                name = p["name"].get(lang, p["name"]["en"])
                desc = p["description"].get(lang, p["description"]["en"])
                phone = p.get("phone", "")
                web = p.get("website", "")
                # Compact: one line per program
                lines.append(f"- **{name}**: {desc[:120]} | {phone} | {web}")
    return SYSTEM_PROMPT.format(programs="\n".join(lines))


# ── Conversation memory ─────────────────────────────────────
sessions: dict[str, list[dict]] = {}


class ChatRequest(BaseModel):
    message: str
    session_id: str = ""
    language: str = "en"


class ChatResponse(BaseModel):
    response: str
    session_id: str
    model: str


# ── NVIDIA NIM inference (primary) ───────────────────────────
async def _nvidia_inference(messages: list[dict]) -> str | None:
    """Call NVIDIA NIM API with Nemotron model."""
    if not NVIDIA_API_KEY:
        return None
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(
                NVIDIA_URL,
                headers={
                    "Authorization": f"Bearer {NVIDIA_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": NVIDIA_MODEL,
                    "messages": messages,
                    "temperature": 0.6,
                    "max_tokens": 2048,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        log.warning(f"NVIDIA NIM HTTP {e.response.status_code}: {e.response.text[:200]}")
        return None
    except Exception as e:
        log.warning(f"NVIDIA NIM failed: {type(e).__name__}: {e}")
        return None


# ── Google Gemini fallback ───────────────────────────────────
async def _gemini_fallback(messages: list[dict]) -> str | None:
    """Call Gemini 2.5 Flash via Google GenAI API."""
    if not GOOGLE_API_KEY:
        return None
    try:
        from google import genai

        client = genai.Client(api_key=GOOGLE_API_KEY)

        # Convert messages to Gemini format
        system_text = ""
        contents = []
        for msg in messages:
            if msg["role"] == "system":
                system_text = msg["content"]
            elif msg["role"] == "user":
                contents.append({"role": "user", "parts": [{"text": msg["content"]}]})
            elif msg["role"] == "assistant":
                contents.append({"role": "model", "parts": [{"text": msg["content"]}]})

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config={
                "system_instruction": system_text,
                "temperature": 0.6,
                "max_output_tokens": 2048,
            },
        )
        return response.text
    except Exception as e:
        log.warning(f"Gemini fallback failed: {e}")
        return None


# ── Chat endpoint ────────────────────────────────────────────
@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    sid = req.session_id or str(uuid.uuid4())

    # Init or retrieve conversation
    if sid not in sessions:
        sessions[sid] = [
            {"role": "system", "content": _build_system_prompt(req.language)}
        ]

    history = sessions[sid]
    history.append({"role": "user", "content": req.message})

    # Try NVIDIA NIM (Nemotron) first
    response_text = await _nvidia_inference(history)
    model_used = NVIDIA_MODEL

    # Fallback to Gemini
    if not response_text:
        response_text = await _gemini_fallback(history)
        model_used = "gemini-2.5-flash"

    # Last resort
    if not response_text:
        model_used = "none"
        response_text = (
            "I'm having trouble connecting right now. "
            "Please call 211 (305-358-4357) for immediate help — "
            "they're available 24/7 in English, Spanish, and Creole."
        )

    # Save assistant response to history
    history.append({"role": "assistant", "content": response_text})

    # Cap history at 20 messages to avoid token limits
    if len(history) > 21:
        sessions[sid] = [history[0]] + history[-20:]

    log.info(f"[{sid[:8]}] model={model_used} lang={req.language}")

    return ChatResponse(response=response_text, session_id=sid, model=model_used)


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "models": {
            "primary": NVIDIA_MODEL,
            "fallback": "gemini-2.5-flash",
        },
        "nvidia_key": bool(NVIDIA_API_KEY),
        "google_key": bool(GOOGLE_API_KEY),
        "programs": len(PROGRAMS),
    }


# Serve static frontend
web_dir = os.path.join(os.path.dirname(__file__), "web")
if os.path.isdir(web_dir):
    app.mount("/", StaticFiles(directory=web_dir, html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
