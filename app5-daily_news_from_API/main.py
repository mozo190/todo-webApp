import requests
from data import NEWS_API_URL, NEWS_API_KEY

api = NEWS_API_KEY
url = NEWS_API_URL

request = requests.get(url)
content = request.text
print(content)
