#!/usr/bin/env python3

import json
import os
import sys

import requests

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

api_key_path = os.path.join(script_dir, 'my_api_key.txt')
chat_id_path = os.path.join(script_dir, 'my_chat_id.txt')

with open(api_key_path, 'r') as f:
    TELEGRAM_TOKEN = f.read().strip()

with open(chat_id_path, 'r') as f:
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
    response = json.dumps(response, indent=2)
    print(response)

