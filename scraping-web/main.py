import requests
import selectorlib

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


def send_email():
    print("Sending email")


def store(extracted_data):
    with open('data.txt', 'a') as file:
        file.write(extracted_data + '\n')


if __name__ == "__main__":
    scraped = scrape(PAGE_URL)
    extracted = extract_data(scraped)
    print(extracted)
    store(extracted)
    if extracted != "No Upcoming tours":
        if extracted not in "data.txt":
            send_email()
