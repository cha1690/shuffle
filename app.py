from flask import Flask, render_template,session
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
import os

app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm('/signup')
    return render_template('signup.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm('/login')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    with app.test_request_context("/"):
        session["key"] = "value"
    app.run()
