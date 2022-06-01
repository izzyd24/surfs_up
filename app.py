# import our flask dependency
from cProfile import run
from flask import Flask
# create the flask app instance
# name denotes name of current function; its a variable 'magic method'
# this should tell us where code is being ran or if imported into another code
app = Flask(__name__)

# create first route
@app.route('/')
def hello_world():
    return 'hello world'

# run these in gitbash
# set FLASK_APP = app.py
# flask run

