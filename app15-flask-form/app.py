
from flask import Flask, request, render_template

app = Flask(__name__)

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