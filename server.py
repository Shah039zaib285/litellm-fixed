from flask import Flask, request, jsonify
import os

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

@app.route("/")
def home():
    return "LiteLLM placeholder - running on Render"

@app.route("/v1/generate", methods=["POST"])
def generate():
    data = request.json or {}
    prompt = data.get("prompt", "")
    # Placeholder response - aap Gemini API call integrate kar sakte ho
    return jsonify({"reply": f"Echo (placeholder): {prompt}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
