import os

import requests

API_key = os.environ.get('WEATHER_API_KEY')


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    responses = requests.get(url)
    data = responses.json()
    filtered_data = data['list'][:forecast_days * 8]
    print(filtered_data)
    return filtered_data


if __name__ == '__main__':
    print(get_data('Tokyo', 3))
