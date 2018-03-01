from flask import Flask 

#creates a instance of the Flask class
app = Flask(__name__)

from app import routes


