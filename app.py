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
@app.route("/api/v1.0/welcome")
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
    # use jsonify function to fomrat in JSON structured file
    # it will help us go through the data easily
    return jsonify(precip)

# create third route; stations 9.5.4
@app.route("/api/v1.0/stations")
def stations():
    # unravel results in 1 dimensional array
    results = session.query(Station.station).all()
    # once unraveled make into list...
    # convert our array into list
    stations = list(np.ravel(results))
    # once again return in JSON format
    return jsonify(stations=stations)

# create the fourth route; monthly temp. 9.5.6
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # calculate the date one year ago from last date in database
    prev_year = dt.date(2017, 8, 23) -dt.timedelta(days=365)

    # query primary station for all temp observations in prev year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    # unravel results into 1D array, then make into list
    # then last return as JSON format
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create fifth route; stats 9.5.6
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# add param of start and end
def descrip_stats(start=None, end=None):
    # create query to select min, max, average temps
    specstats = [func.min(Measurement.tobs). 
    func.average(Measurement.tobs), func.max(Measurement.tobs)]

    # use if not to find start and end date
    if not end: 
        results = session.query(*specstats).\
            filter(Measurement.date >= start).all()
        # after if/not, unravel 1d array into list
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    # now calc min, avg, max for start and end dates 
    results = session.query(*specstats).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


# run this in gitbash
# set FLASK_APP = app.py
# flask run
