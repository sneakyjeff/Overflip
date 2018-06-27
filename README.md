## PROJECT TITLE: 
Flask tutorial with CRUD functionality following miguel grinberg

### INPROGRESS

'''
CURRENT PROJECT STRUCTURE TO DATE:
FlaskOverflip/
  venv/
  app/
    __init__.py
    routes.
    forms.py
    templates/
      base.html
      index.html
      login.html
      payment.html
  migrations/
  config.py
  overflip.py
  readme.md
'''

## PACKAGES NEEDED TO RUN FILES
>Python3

Flask (using pip)

Setup Virtual enviroment (A virtual enviroment is essentially a copy of the Python intrepret. We can install and download any sort of packages and only affect this virtual enviroment rather than download packages for the system wide Python version)
python3 -m venv venv (Creates a virtual enviroment using the venv command and names it venv)

source venv/bin/activate to activate/enter enviroment

deactivate to exit virtual enviroment

source venv/bin/activate
export FLASK_APP=overflip.py
FLASK_DEBUG=1 flask run

To handle web forms, using flask-wtf extension
pip install flask-wtf

using flask-sqlalchemy
pip install flask-sqlalchemy


## Features to add:
be able to delete users
