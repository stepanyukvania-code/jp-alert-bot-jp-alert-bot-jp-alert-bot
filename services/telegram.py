import requests
import os


TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    r = requests.post(url, data=data)

    print("TELEGRAM STATUS:", r.status_code)
    print("TELEGRAM RESPONSE:", r.text)
