"""
Miami Resources — Production Server

FastAPI wrapper that:
1. Serves the static web frontend
2. Exposes /api/chat that proxies to the Google ADK agent
"""

import os
import uuid

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from pydantic import BaseModel

from miami_resources.agent import root_agent

app = FastAPI(title="Miami Resources", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name="miami_resources", session_service=session_service)

USER_ID = "web_user"


class ChatRequest(BaseModel):
    message: str
    session_id: str = ""
    language: str = "en"


class ChatResponse(BaseModel):
    response: str
    session_id: str


@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    sid = req.session_id or str(uuid.uuid4())

    session = await session_service.get_session(
        app_name="miami_resources", user_id=USER_ID, session_id=sid
    )
    if session is None:
        session = await session_service.create_session(
            app_name="miami_resources", user_id=USER_ID, session_id=sid
        )

    from google.genai.types import Content, Part

    user_content = Content(
        role="user",
        parts=[Part(text=f"[Language: {req.language}] {req.message}")],
    )

    response_text = ""
    async for event in runner.run_async(
        user_id=USER_ID, session_id=sid, new_message=user_content
    ):
        if event.is_final_response() and event.content and event.content.parts:
            response_text = "\n".join(
                p.text for p in event.content.parts if p.text
            )

    return ChatResponse(response=response_text or "I couldn't process that request. Please try again or call 211.", session_id=sid)


# Serve static frontend
web_dir = os.path.join(os.path.dirname(__file__), "web")
if os.path.isdir(web_dir):
    app.mount("/", StaticFiles(directory=web_dir, html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
