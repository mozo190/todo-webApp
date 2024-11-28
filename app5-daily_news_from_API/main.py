import requests
from data import NEWS_API_URL, NEWS_API_KEY

api = NEWS_API_KEY
url = NEWS_API_URL

request = requests.get(url)
content = request.json()
for i in content['articles']:
    print(i['title'])
    print(i['description'])
    print(i['url'])
    print()
