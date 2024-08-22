#!/usr/bin/env python3

import sys

import requests

with open('./my_api_key.txt', 'r') as f:
    TELEGRAM_TOKEN = f.read().strip()

with open('./my_chat_id.txt', 'r') as f:
    CHAT_ID = f.read().strip()

API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

def send_telegram_message(message):
    """Send a message to a Telegram chat via bot"""
    data = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(API_URL, data=data)
    return response.json()

if __name__ == "__main__":
    message = "Your command has completed successfully!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    response = send_telegram_message(message)
    print(response)
    print("Notification sent.")

