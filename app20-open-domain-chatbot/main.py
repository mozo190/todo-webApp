from flask import Flask, request, jsonify
import requests
import openai

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "your_facebook_page_access_token"
VERIFY_TOKEN = "your_facebook_verification_token"
OPENAI_API_KEY = "your_openai_api_key"

openai.api_key = OPENAI_API_KEY