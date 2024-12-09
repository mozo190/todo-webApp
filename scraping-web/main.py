import ssl
import time

import requests
import selectorlib
import smtplib

PASSWORD = "password"
EMAIL_ = "mozo37@gmail.com"
to_email = "mozo37@gmail.com"

PAGE_URL = "https://programmer100.pythonanywhere.com/tours/"
URL_DATA = "/html/body/div[1]/div/h1[3]"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


# Scraping the data
def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source_text = response.text
    return source_text


def extract_data(source_):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    data = extractor.extract(source_)['tours']
    return data


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(EMAIL_, PASSWORD)

        server.sendmail(EMAIL_, to_email, message)
        print("Email sent successfully")


def store(extracted_data):
    with open('data.txt', 'a') as file:
        file.write(extracted_data + '\n')


def read_data(extracted_data):
    with open('data.txt', 'r') as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped = scrape(PAGE_URL)
        extracted = extract_data(scraped)
        print(extracted)

        content = read_data(extracted)
        if extracted != "No Upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="New events was found")
        time.sleep(2)