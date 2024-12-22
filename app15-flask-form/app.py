from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email_address = db.Column(db.String(100))
    date_input = db.Column(db.String(100))
    current_position = db.Column(db.String(100))


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_address = request.form['email']
        date_input = request.form['date']
        current_position = request.form['occupation']
        print(first_name, last_name, email_address, date_input, current_position)
    return render_template('index.html')


app.run(debug=True, port=5001)
