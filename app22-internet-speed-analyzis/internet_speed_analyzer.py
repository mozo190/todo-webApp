from flask import Flask, render_template

app = Flask(__name__)

speed_data = []


@app.route('/')
def index():
    return render_template('HTML_TEMPLATE.html')


@app.route('/speedtest')
def speedtest():
    return 'Speedtest'


if __name__ == '__main__':
    app.run(debug=True)
