from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db, ma
from flask import Response
from flask import Flask, jsonify, current_app
from flaskr.models import AirPassenger, AirPassengerScheme
# import json

air_shema =  AirPassengerScheme()

@app.route('/')
def show_data():
    airpassenger=AirPassenger.query.all()
    with app.app_context():
        result=air_shema.jsonify(airpassenger)
        resp=Response(result, status=200, mimetype='application/json')
    return resp
    # return render_template('show_data.html', result=result)
