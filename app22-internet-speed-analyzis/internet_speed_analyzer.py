from flask import Flask

app = Flask(__name__)

speed_data = []


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/speedtest')
def speedtest():
    return 'Speedtest'


if __name__ == '__main__':
    app.run(debug=True)
