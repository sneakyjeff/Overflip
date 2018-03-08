from flask import Flask, url_for, request, redirect 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#creates a instance of the Flask class
app = Flask(__name__)
#flask instance has a config attribute that can be modified described here http://flask.pocoo.org/docs/0.12/config/
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
#this url_for('index') is the redirection after user logs in. Change this once you decide what the login page to look like
login.login_view = 'login'

from app import routes, models


