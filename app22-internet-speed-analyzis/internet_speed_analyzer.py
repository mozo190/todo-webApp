from flask import Flask, render_template, jsonify

app = Flask(__name__)

speed_data = []


@app.route('/')
def index():
    return render_template('HTML_TEMPLATE.html')


@app.route('/speedtest')
def speedtest():
    timestamps = [data['timestamp'] for data in speed_data]
    download_speeds = [data['download_speed'] for data in speed_data]
    upload_speeds = [data['upload_speed'] for data in speed_data]
    return jsonify({
        'timestamps': timestamps,
        'download_speeds': download_speeds,
        'upload_speeds': upload_speeds
    })


if __name__ == '__main__':
    app.run(debug=True)
