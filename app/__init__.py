from flask import Flask 
from config import Config

#creates a instance of the Flask class
app = Flask(__name__)
app.config.from_object(Config)

from app import routes


