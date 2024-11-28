import requests

from data import NEWS_API_URL, NEWS_API_KEY, E_MAIL
from send_email import send_email

api = NEWS_API_KEY
url = NEWS_API_URL

request = requests.get(url)
content = request.json()

body = ""
for i in content['articles']:
    if i['title'] and i['description'] and i['url'] is not None:
        body += i['title'] + '\n' + i['description'] + '\n' + i['url'] + '\n\n'

body = body.encode('utf-8')
send_email(body, E_MAIL)
