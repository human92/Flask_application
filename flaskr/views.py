from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import AirPassenger

@app.route('/')
def show_data():
    # airpassenger = AirPassenger.query(AirPassenger.id.desc()).all()
    airpassenger = AirPassenger.query(AirPassenger.TravelDate, AirPassenger.Passengers).all()
    return render_template('\templates\show_data.html', airpassenger=airpassenger)
