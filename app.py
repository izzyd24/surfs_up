# import our flask dependency
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from cProfile import run
import app

# set up the database engine 
# create enginge lets us access the sqlite databse
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# saves references to each table with variable for each class to use later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from Py to our database
session = Session(engine)

# define the flask app 
app = Flask(__name__)

# create welcome route 9.5.2
@app.route("/")
def welcome():
    # use /api/v1.0/ as naming convention followed by name of our wanted route
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# create second route; precipitation 9.5.3
@app.route("/api/v1.0/precipitation")
def precipitation():
    # calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and the precipitation as the value 
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# create third route; stations 9.5.4

# run this in gitbash
# set FLASK_APP = app.py
# flask run

