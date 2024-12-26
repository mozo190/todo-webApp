import threading
import time

from flask import Flask, render_template, jsonify
from speedtest import Speedtest

app = Flask(__name__)

speed_data = []


@app.route('/')
def index():
    return render_template('HTML_TEMPLATE.html')


@app.route('/speedtest')
def get_data():
    timestamps = [data['timestamp'] for data in speed_data]
    download_speeds = [data['download_speed'] for data in speed_data]
    upload_speeds = [data['upload_speed'] for data in speed_data]
    return jsonify({
        'timestamps': timestamps,
        'download_speeds': download_speeds,
        'upload_speeds': upload_speeds
    })


def measure_speed():
    tester = Speedtest()
    while True:
        tester.get_best_server()
        download_speed = tester.download() / 1_000_000  # Convert to Mbps
        upload_speed = tester.upload() / 1_000_000  # Convert to Mbps
        speed_data.append({
            'timestamp': time.strftime('%H:%M:%S'),
            'download_speed': download_speed,
            'upload_speed': upload_speed
        })
        if len(speed_data) > 50:  # Keep only the last 50 data points
            speed_data.pop(0)
        time.sleep(10)  # Measure speed every 10 seconds


if __name__ == '__main__':
    threading.Thread(target=measure_speed, daemon=True).start()
    app.run(debug=True)
