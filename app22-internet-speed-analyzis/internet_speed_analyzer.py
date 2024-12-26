from flask import Flask

app = Flask(__name__)

speed_data = []

if __name__ == '__main__':
    app.run(debug=True)
