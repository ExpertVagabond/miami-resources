/**
 * Miami Resources — Chat UI
 *
 * Connects to the FastAPI backend (/api/chat) which wraps
 * the Google ADK multi-agent system.
 */

const API_URL = window.location.origin + "/api/chat";
const messagesEl = document.getElementById("messages");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");

let currentLang = "en";
let sessionId = crypto.randomUUID();

// ── i18n ────────────────────────────────────────────────────
const translations = {
  en: {
    tagline: "Free programs for Miami-Dade residents",
    "cat-housing": "Housing",
    "cat-food": "Food",
    "cat-healthcare": "Healthcare",
    "cat-jobs": "Jobs",
    "cat-education": "Education",
    "cat-crisis": "Crisis",
    welcome:
      "Welcome to Miami Resources! I can help you find free programs for housing, food, healthcare, jobs, and education in Miami-Dade County. What do you need help with?",
    "input-placeholder": "Type your question...",
    "footer-crisis":
      '<strong>Crisis?</strong> Call 911 &bull; 211 Helpline: <a href="tel:3053584357">305-358-4357</a> &bull; Suicide: <a href="tel:988">988</a>',
  },
  es: {
    tagline: "Programas gratuitos para residentes de Miami-Dade",
    "cat-housing": "Vivienda",
    "cat-food": "Alimentos",
    "cat-healthcare": "Salud",
    "cat-jobs": "Empleo",
    "cat-education": "Educación",
    "cat-crisis": "Crisis",
    welcome:
      "\u00a1Bienvenido a Miami Resources! Puedo ayudarte a encontrar programas gratuitos de vivienda, alimentos, salud, empleo y educaci\u00f3n en el condado de Miami-Dade. \u00bfEn qu\u00e9 puedo ayudarte?",
    "input-placeholder": "Escribe tu pregunta...",
    "footer-crisis":
      '<strong>\u00bfCrisis?</strong> Llame 911 &bull; L\u00ednea 211: <a href="tel:3053584357">305-358-4357</a> &bull; Suicidio: <a href="tel:988">988</a>',
  },
  ht: {
    tagline: "Pwogram gratis pou rezidan Miami-Dade",
    "cat-housing": "Lojman",
    "cat-food": "Manje",
    "cat-healthcare": "Sante",
    "cat-jobs": "Travay",
    "cat-education": "Edikasyon",
    "cat-crisis": "Kriz",
    welcome:
      "Byenveni nan Miami Resources! Mwen ka ede w jwenn pwogram gratis pou lojman, manje, sante, travay, ak edikasyon nan Konte Miami-Dade. Kisa ou bezwen \u00e8d?",
    "input-placeholder": "Ekri kesyon ou...",
    "footer-crisis":
      '<strong>Kriz?</strong> Rele 911 &bull; Liy \u00c8d 211: <a href="tel:3053584357">305-358-4357</a> &bull; Swisid: <a href="tel:988">988</a>',
  },
};

function setLanguage(lang) {
  currentLang = lang;
  document.documentElement.lang = lang;

  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
  });

  const t = translations[lang] || translations.en;
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.dataset.i18n;
    if (t[key]) el.innerHTML = t[key];
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const key = el.dataset.i18nPlaceholder;
    if (t[key]) el.placeholder = t[key];
  });
}

// ── Category quick actions ──────────────────────────────────
const categoryPrompts = {
  en: {
    housing: "I need help finding housing assistance",
    food: "I need help finding food assistance",
    healthcare: "I need help finding healthcare",
    jobs: "I need help finding a job",
    education: "I need help with education programs",
    crisis: "I'm in a crisis and need immediate help",
  },
  es: {
    housing: "Necesito ayuda para encontrar asistencia de vivienda",
    food: "Necesito ayuda para encontrar asistencia alimentaria",
    healthcare: "Necesito ayuda para encontrar atención médica",
    jobs: "Necesito ayuda para encontrar empleo",
    education: "Necesito ayuda con programas de educación",
    crisis: "Estoy en crisis y necesito ayuda inmediata",
  },
  ht: {
    housing: "Mwen bezwen èd pou jwenn asistans lojman",
    food: "Mwen bezwen èd pou jwenn asistans manje",
    healthcare: "Mwen bezwen èd pou jwenn swen sante",
    jobs: "Mwen bezwen èd pou jwenn travay",
    education: "Mwen bezwen èd ak pwogram edikasyon",
    crisis: "Mwen nan yon kriz epi mwen bezwen èd imedyatman",
  },
};

// ── Message rendering ───────────────────────────────────────
function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = `msg msg--${sender}`;

  const bubble = document.createElement("div");
  bubble.className = "msg__bubble";

  // Simple markdown-ish rendering for bot messages
  if (sender === "bot") {
    bubble.innerHTML = formatBotText(text);
  } else {
    bubble.textContent = text;
  }

  msg.appendChild(bubble);
  messagesEl.appendChild(msg);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function addTypingIndicator() {
  const msg = document.createElement("div");
  msg.className = "msg msg--bot msg--typing";
  msg.id = "typing";

  const bubble = document.createElement("div");
  bubble.className = "msg__bubble";
  bubble.innerHTML =
    '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>';

  msg.appendChild(bubble);
  messagesEl.appendChild(msg);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function removeTypingIndicator() {
  const el = document.getElementById("typing");
  if (el) el.remove();
}

function formatBotText(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(
      /\[([^\]]+)\]\((https?:\/\/[^\)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener">$1</a>'
    )
    .replace(/(https?:\/\/[^\s<]+)/g, (url, match, offset, str) => {
      // Don't double-link URLs already in anchor tags
      const before = str.substring(Math.max(0, offset - 6), offset);
      if (before.includes('href="') || before.includes("'>")) return url;
      return `<a href="${url}" target="_blank" rel="noopener">${url}</a>`;
    })
    .replace(
      /(\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})/g,
      '<a href="tel:$1">$1</a>'
    )
    .replace(/\n/g, "<br>");
}

// ── API communication ───────────────────────────────────────
async function sendMessage(text) {
  addMessage(text, "user");
  addTypingIndicator();
  userInput.value = "";
  userInput.disabled = true;

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: text,
        session_id: sessionId,
        language: currentLang,
      }),
    });

    removeTypingIndicator();

    if (!res.ok) {
      throw new Error(`Server error: ${res.status}`);
    }

    const data = await res.json();
    addMessage(data.response || data.message || "No response received.", "bot");
  } catch (err) {
    removeTypingIndicator();
    console.error("Chat error:", err);

    const errorMessages = {
      en: "Sorry, I'm having trouble connecting. Please try again, or call 211 for immediate help.",
      es: "Lo siento, tengo problemas de conexión. Inténtelo de nuevo, o llame al 211 para ayuda inmediata.",
      ht: "Eskize m, mwen gen pwoblèm koneksyon. Tanpri eseye ankò, oswa rele 211 pou èd imedya.",
    };
    addMessage(errorMessages[currentLang] || errorMessages.en, "bot");
  } finally {
    userInput.disabled = false;
    userInput.focus();
  }
}

// ── Event listeners ─────────────────────────────────────────
chatForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = userInput.value.trim();
  if (text) sendMessage(text);
});

document.querySelectorAll(".lang-btn").forEach((btn) => {
  btn.addEventListener("click", () => setLanguage(btn.dataset.lang));
});

document.querySelectorAll(".cat-pill").forEach((btn) => {
  btn.addEventListener("click", () => {
    const cat = btn.dataset.category;
    const prompts = categoryPrompts[currentLang] || categoryPrompts.en;
    const text = prompts[cat];
    if (text) sendMessage(text);
  });
});

// Init
setLanguage("en");
