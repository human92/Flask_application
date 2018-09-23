from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import AirPassenger

@app.route('/')
def show_data():
   airpassenger = AirPassenger.query.all()
   return render_template('show_data.html', airpassenger=airpassenger)

