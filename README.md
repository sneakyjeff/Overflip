DATE: 02/27/2018

PROJECT TITLE: 
Flask tutorial with CRUD functionality setup by following instructions from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

CURRENT PROJECT STRUCTURE SO FAR:
FlaskOverflip/
  venv/
  app/
    __init__.py
    routes.py
  overflip.py

NEEDED INSTALLATION:
>Python3

Flask (using pip)

Setup Virtual enviroment (A virtual enviroment is essentially a copy of the Python intrepret. We can install and download any sort of packages and only affect this virtual enviroment rather than download packages for the system wide Python version)
python3 -m venv venv (Creates a virtual enviroment using the venv command and names it venv)

source venv/bin/activate to activate/enter enviroment

deactivate to exit virtual enviroment

export FLASK_APP=overflip.py
flask run