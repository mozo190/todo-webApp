import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)


@app.route('/')
def home():
    return render_template("home.html", data=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {f"Station": station,
            f"Date": date,
            f"Temperature": temperature}


@app.route('/api/v1/<station>')
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    return {f"Station": station,
            f"Data": df.to_dict(orient="records")}


@app.route('/api/v1/yearly/<station>/<year>')
def year_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df['    DATE'].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))]
    return {f"Station": station,
            f"Year": year,
            f"Data": result.to_dict(orient="records")}


if __name__ == '__main__':
    app.run(debug=True)
