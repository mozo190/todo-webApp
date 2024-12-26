# Flask Facebook Messenger Bot with OpenAI GPT-3

This project is a Flask-based web application that integrates with Facebook Messenger and OpenAI GPT-3. The bot is able
to chat with users on Facebook Messenger and generate responses using OpenAI GPT-3.

## Prerequisites

Before running the application, you need to have the following:

* Python 3.6 or higher
* Facebook Developer Account
* OpenAI Python Client
* OpenAI API Key
* Ngrok (for local development)
* Flask
* Requests

## Installation

1. Clone the repository:

```bash
git clone
```

2. Install the required Python packages:

```bash 
pip install -r requirements.txt
```

3. Set up a Facebook App and Page:
4. Set up a webhook for the Facebook Messenger bot:
5. Set up OpenAI GPT-3 API:
6. Run the Flask application:

```bash
python app.py
```

7. Run Ngrok to expose the local server to the internet:

```bash
ngrok http 5000
```

8. Update the Facebook Messenger webhook URL with the Ngrok URL:

```bash
https://<ngrok_url>/webhook
```

9. Chat with the Facebook Messenger bot!
10. Generate responses using OpenAI GPT-3!
11. Enjoy!
12. Happy coding!

## Endpoints:

* 'GET /webhook' - Verify the Facebook Messenger webhook
* 'POST /webhook' - Receive messages from Facebook Messenger
* 'POST /generate' - Generate responses using OpenAI GPT-3

## Functions:

* 'send_message(recipient_id, message_text)' - Send a message to a user on Facebook Messenger
* 'generate_response(user_message)' - Generate a response using OpenAI GPT-3

## License

This project is licensed under the MIT License - see the LICENSE file for details.

