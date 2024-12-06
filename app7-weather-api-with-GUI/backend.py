import os

import requests

API_key = os.environ.get('WEATHER_API_KEY')


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    responses = requests.get(url)
    data = responses.json()
    filtered_data = data['list'][:forecast_days * 8]
    if kind == 'Temperature':
        return [d['main']['temp'] - 273.15 for d in filtered_data]
    elif kind == 'Humidity':
        return [d['main']['humidity'] for d in filtered_data]
    elif kind == 'Wind Speed':
        return [d['wind']['speed'] for d in filtered_data]
    elif kind == 'Pressure':
        return [d['main']['pressure'] for d in filtered_data]
    elif kind == "Sky":
        return [d['weather'][0]['main'] for d in filtered_data]


if __name__ == '__main__':
    print(get_data('Mumbai', 3, 'Temperature'))
