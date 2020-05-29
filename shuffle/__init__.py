from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_mail import Mail
from flask_heroku import Heroku

import psycopg2
import os
from apiclient.discovery import build

app = Flask(__name__)
csrf = CSRFProtect(app)
heroku = Heroku(app)
csrf.init_app(app)
app.config.update(SECRET_KEY=os.urandom(24))
app.config['CSRF_ENABLED'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = None

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'URI'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'basic'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
mail = Mail(app)
DEVELOPER_KEY = "developer key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube_object = build(YOUTUBE_API_SERVICE_NAME,
                       YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)

from shuffle import routes
