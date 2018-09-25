from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db, ma
from flask import Flask, jsonify, current_app
from flaskr.models import AirPassenger, AirPassengerScheme
# import json

air_shema =  AirPassengerScheme()

@app.route('/')
def show_data():
    airpassenger=AirPassenger.query.all()
    with app.app_context():
        result=air_shema.jsonify(airpassenger)
    return render_template('show_data.html', result=result)

