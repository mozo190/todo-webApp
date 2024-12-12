import sqlite3
from datetime import datetime

import requests
import selectorlib

# Connecting to the database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute(" CREATE TABLE IF NOT EXISTS events (date TEXT, temperature REAL)")

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source_text = response.text
    return source_text


def extract_data(source_text):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    data_ = extractor.extract(source_text)['tours']
    print(data_)
    return data_


def send_email(message):
    print("Email sent successfully")


def store(extracted_data):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO events VALUES (?, ?)", (now, extracted_data))
    connection.commit()


def read_data():
    cursor.execute("SELECT * FROM events")
    datas = cursor.fetchall()
    print(datas)
    return datas


if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract_data(scraped)
    store(extracted)
