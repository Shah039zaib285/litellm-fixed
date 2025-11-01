from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "LiteLLM Fixed API Running!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    # Simple echo + pretend AI
    reply = f"Mega Agency: Aapka message mila — '{user_msg}'. Shopify store creation ke liye 4000 PKR total hai, 1000 PKR advance aur 3000 PKR baad mein."
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
