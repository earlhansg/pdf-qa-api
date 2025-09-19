import requests
import os
from flask import Blueprint, request, jsonify

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    payload = {
        "model": "llama2:latest",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ],
        "stream": False  # 🚀 disable streaming
    }

    response = requests.post(os.getenv("OLLAMA_URL"), json=payload)

    result = response.json()
    reply = result.get("message", {}).get("content", "")

    return jsonify({"answer": reply})
