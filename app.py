from flask import Flask, render_template,session, flash, redirect, request, url_for
from forms import RegistrationForm, LoginForm
from flask_session import Session
import os

app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm('/signup')
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('category'))
    return render_template('signup.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm('/login')
    if form.validate_on_submit():
        if form.email.data == 'email' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    with app.test_request_context("/"):
        session["key"] = "value"
    app.run()
