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

app.config.update(SECRET_KEY=os.urandom(24))
app.config['CSRF_ENABLED'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'shuffleapp8@gmail.com'
app.config['MAIL_PASSWORD'] = '1DpVX5jnQfea'
mail = Mail(app)
DEVELOPER_KEY = "AIzaSyDEgXt5MtD9-J3B1B5x9KlxOnP1etevG6w"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube_object = build(YOUTUBE_API_SERVICE_NAME,
                       YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)

from shuffle import routes