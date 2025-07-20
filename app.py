from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = 'توکن رباتت اینجا'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        if text:
            send_message(chat_id, "سلام! حالت چطوره؟ 😊")
    return 'ok'

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

@app.route('/', methods=['GET'])
def index():
    return 'ربات آماده دریافت پیام است.'

if __name__ == '__main__':
    app.run(debug=True)
