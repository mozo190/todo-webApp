from datetime import datetime

from flask import Flask, request, render_template, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = 'mozo37@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email_address = db.Column(db.String(80))
    date_input = db.Column(db.Date)
    current_position = db.Column(db.String(80))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_address = request.form['email']
        date_input = request.form['date']
        date_obj = datetime.strptime(date_input, '%Y-%m-%d')
        current_position = request.form['occupation']

        form = Form(first_name=first_name,
                    last_name=last_name,
                    email_address=email_address,
                    date_input=date_obj,
                    current_position=current_position)
        db.session.add(form)
        db.session.commit()

        msg = Message('Hello',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email_address],
                      body=f'Hello {first_name}, your form submitted successfully.\n' 
                           f'Your current position is {current_position}\n'
                           f'Your date of birth is {date_input}\n'
                           f'Thank You!')
        mail.send(msg)

        flash(f'{first_name}, your form submitted successfully')
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
