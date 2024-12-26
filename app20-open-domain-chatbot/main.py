import openai
import requests
from flask import Flask, request

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


def generate_response(user_message):
    pass


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge
        return 'Invalid verification token', 403

    elif request.method == 'POST':
        data = request.json
        for entry, in data.get('entry', []):
            for message_event in entry.get('messaging', []):
                sender_id = message_event['sender']['id']
                if 'message' in message_event:
                    user_message = message_event['message']['text']
                    bot_response = generate_response(user_message)
                    send_message(sender_id, bot_response)
        return 'ok', 200
