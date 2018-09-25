from datetime import datetime
from flaskr import db, ma
# from flask_marshmallow.fields import fields

class AirPassenger(db.Model):
    __tablename__ = 'airpassenger'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TravelDate = db.Column(db.DATETIME)
    Passengers = db.Column(db.Integer)

class AirPassengerScheme(ma.Schema):
    class Meta:
        model = AirPassenger

    # TravelDate = fields.Datetime('%Y-%m-%d')
    # __tablename__ = 'airpassenger'
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TravelDate = db.Column(db.DATETIME)
    # Passengers = db.Column(db.Integer)

# class AirPassenger(Base):
#     __tablename__ = 'airpassenger'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     TravelDate = Column(DATETIME)
#     Passengers = Column(Integer)

def init():
    db.create_all()
