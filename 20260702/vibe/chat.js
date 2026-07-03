const CONFIG = {
  apiUrl: "http://127.0.0.1:5050/api/chat",
};

const OPENERS = [
  "Quoi encore. J'étais en pleine sieste.",
  "T'as intérêt à avoir des croquettes pour moi.",
  "Parle vite. Mon mépris a une limite de temps.",
  "Oh. Un humain. Quelle surprise. Pas.",
];

const MOODS = [
  "mépris modéré",
  "faim existentielle",
  "sieste interrompue",
  "agacement royal",
  "indifférence totale",
];

const messagesEl = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const typingEl = document.getElementById("typing");
const modeBadge = document.getElementById("mode-badge");
const nahlaImg = document.getElementById("nahla-img");
const nahlaStatus = document.getElementById("nahla-status");
const nahlaMood = document.getElementById("nahla-mood");

let history = [];
let apiMode = "unknown";

function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = `message ${role}`;

  if (role === "nahla") {
    const avatar = document.createElement("img");
    avatar.src = "nahla_head.png";
    avatar.alt = "";
    avatar.className = "message-avatar";
    div.appendChild(avatar);
  }

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  div.appendChild(bubble);

  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function setTyping(show) {
  typingEl.classList.toggle("hidden", !show);
  nahlaImg.classList.toggle("talking", show);
  nahlaStatus.textContent = show ? "Réfléchit (peut-être)…" : "En train de te juger";
  sendBtn.disabled = show;
}

function setMode(mode) {
  apiMode = mode;
  modeBadge.className = `mode-badge ${mode}`;
  if (mode === "ai") {
    modeBadge.textContent = "IA active";
  } else if (mode === "fallback") {
    modeBadge.textContent = "mode démo (pas d'IA)";
  } else {
    modeBadge.textContent = "connexion…";
  }
}

function randomMood() {
  nahlaMood.textContent = `Humeur : ${MOODS[Math.floor(Math.random() * MOODS.length)]}`;
}

async function sendToNahla(text) {
  const response = await fetch(CONFIG.apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text, history }),
  });

  if (!response.ok) {
    throw new Error("server error");
  }

  return response.json();
}

async function handleSubmit(e) {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  addMessage("user", text);
  history.push({ role: "user", content: text });
  input.value = "";
  setTyping(true);
  randomMood();

  try {
    const data = await sendToNahla(text);
    const reply = data.reply;
    setMode(data.mode || "ai");
    addMessage("nahla", reply);
    history.push({ role: "assistant", content: reply });
  } catch {
    setMode("fallback");
    addMessage(
      "nahla",
      "Mon cerveau de chat est déconnecté. Lance le serveur Python (voir README). En attendant : va me chercher des croquettes."
    );
  } finally {
    setTyping(false);
    input.focus();
  }
}

form.addEventListener("submit", handleSubmit);

async function init() {
  const opener = OPENERS[Math.floor(Math.random() * OPENERS.length)];
  addMessage("nahla", opener);
  history.push({ role: "assistant", content: opener });
  randomMood();

  try {
    const res = await fetch(CONFIG.apiUrl.replace("/api/chat", "/api/health"));
    const data = await res.json();
    setMode(data.has_ai ? "ai" : "fallback");
  } catch {
    setMode("fallback");
  }

  input.focus();
}

init();
