from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    temperature = 25
    return {f"Station": station,
            f"Date": date,
            f"Temperature": temperature}


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)