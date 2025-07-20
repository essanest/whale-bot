from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7988601127:AAFXcCLC94rdXTMNQ_YudTL0VqPBjuhdQ1w"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text.lower() in ["سلام", "salam"]:
            requests.post(URL, json={
                "chat_id": chat_id,
                "text": "سلام! حالت چطوره؟ 😊"
            })

    return {"ok": True}

if __name__ == "__main__":
    app.run(port=5000)