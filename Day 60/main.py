from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    name = request.form['Name']
    password = request.form['Password']
    return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == '__main__':
    app.run()
