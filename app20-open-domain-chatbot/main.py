import openai
import requests
from flask import Flask

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "your_facebook_page_access_token"
VERIFY_TOKEN = "your_facebook_verification_token"
OPENAI_API_KEY = "your_openai_api_key"

openai.api_key = OPENAI_API_KEY


def send_message(recipient_id, message_text):
    """Send a message to the user via Facebook Messenger"""
    url = f'https://graph.facebook.com/v12.0/me/messages?access_token={PAGE_ACCESS_TOKEN}'
    headers = {'Content-Type': 'application/json'}
    data = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text}
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print('Failed to send message:', response.text, response.status_code)
