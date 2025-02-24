from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length
import os


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField('Password', validators=[Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField('Login')

app = Flask(__name__)
app.secret_key = os.urandom(24)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.validate_on_submit():
            if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
                return render_template('success.html')
            else:
                return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
