import os
from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7988601127:AAFXcCLC94rdXTMNQ_YudTL0VqPBjuhdQ1w'
CHAT_ID = '256764836'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        wallet = data.get("wallet")
        token = data.get("token")
        tx_hash = data.get("tx_hash")

        message = f"🚨 Whale Alert!\nWallet: `{wallet}`\nToken: `{token}`\nTX: https://solscan.io/tx/{tx_hash}"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        requests.post(TELEGRAM_API_URL, json=payload)

        return {'ok': True}, 200
    except Exception as e:
        return {'ok': False, 'error': str(e)}, 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
