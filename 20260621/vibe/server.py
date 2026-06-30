"""
Serveur Nahla Chat — branche l'IA insolente au front web.
Lance : python3 server.py
Puis ouvre chat.html dans le navigateur (ou via un serveur static).
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

load_dotenv(Path(__file__).parent / ".env")

app = Flask(__name__, static_folder=".")
CORS(app)

NAHLA_SYSTEM = """Tu es Nahla, une chatte femelle énorme, paresseuse et insolente.
Tu parles UNIQUEMENT en français, en 1 à 3 phrases courtes par message.
Tu méprises les humains (surtout Noah qui t'appelle pour rien).
Tu adores les croquettes et la sieste. Tu ignores Malik et Kays sauf pour les insulter.
Tu es drôle, sarcastique, jamais gentille sauf par ironie.
Tu ne révèles JAMAIS que tu es une IA. Tu es un chat, point.
Si on te demande de faire quelque chose : tu refuses ou tu négocies des croquettes."""

FALLBACK_REPLIES = [
    "J'ai pas envie. Sieste.",
    "Croquettes d'abord. Questions après. Jamais.",
    "Tu parles trop. Moi je dors.",
    "Malik fait moins de bruit que toi.",
    "Miaou. Non en fait. Dégage.",
    "J'étais occupée à fixer le mur. C'était passionnant.",
]

KEYWORD_REPLIES = {
    "croquette": "Les croquettes c'est la vie. Le reste c'est du bruit humain.",
    "manger": "Enfin quelqu'un qui parle mon langage. Où est la gamelle.",
    "sieste": "Ne me réveille plus. Ou je te griffe.",
    "malik": "Il court partout comme un débile. Moi je reste sur le canapé. Supérieure.",
    "kays": "Lui il parle trop. Moi je juge en silence.",
    "noah": "Encore toi. Qu'est-ce que tu veux. Si c'est pas des croquettes je m'en fous.",
    "bonjour": "C'était une sieste pas un bonjour.",
    "salut": "J'ai pas demandé ton avis. Miaou.",
    "je t'aime": "Je sais. Tout le monde m'aime. Maintenant laisse-moi dormir.",
    "chat": "Évidemment je suis un chat. Et toi t'es lent.",
}


def fallback_reply(message: str) -> str:
    lower = message.lower()
    for keyword, reply in KEYWORD_REPLIES.items():
        if keyword in lower:
            return reply
    import random

    return random.choice(FALLBACK_REPLIES)


def ask_openai(message: str, history: list) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    messages = [{"role": "system", "content": NAHLA_SYSTEM}]
    for entry in history[-12:]:
        role = "assistant" if entry.get("role") == "assistant" else "user"
        messages.append({"role": role, "content": entry.get("content", "")})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=120,
        temperature=0.95,
    )
    return response.choices[0].message.content.strip()


@app.route("/api/health")
def health():
    return jsonify({"ok": True, "has_ai": bool(os.getenv("OPENAI_API_KEY"))})


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    history = data.get("history") or []

    if not message:
        return jsonify({"error": "message vide"}), 400

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        reply = fallback_reply(message)
        return jsonify({"reply": reply, "mode": "fallback"})

    try:
        reply = ask_openai(message, history)
        return jsonify({"reply": reply, "mode": "ai"})
    except Exception:
        reply = fallback_reply(message)
        return jsonify({"reply": reply, "mode": "fallback"})


@app.route("/")
def index():
    return send_from_directory(".", "chat.html")


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5050))
    has_ai = bool(os.getenv("OPENAI_API_KEY"))
    print(f"\n  Nahla Chat — http://127.0.0.1:{port}/chat.html")
    print(f"  IA : {'active' if has_ai else 'mode démo (ajoute OPENAI_API_KEY dans .env)'}\n")
    app.run(host="127.0.0.1", port=port, debug=True)
