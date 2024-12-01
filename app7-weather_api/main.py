from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)

@app.route('/')
def home():
    return render_template("home.html", data=stations)


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {f"Station": station,
            f"Date": date,
            f"Temperature": temperature}


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)