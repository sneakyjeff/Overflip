import os
basedir = os.path.abspath(os.path.dirname(__file__))


#SQLALCHMEY_DATABASE_URI line tells the code where our database is and what type it is.
#The URI line takes in a string and that string format is based off what database type we are working with
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False