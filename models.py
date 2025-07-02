from flask_sqlalchemy import  SQLAlchemy 
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String, nullable = False)
    fullname = db.Column(db.String, unique = True, nullable = False)
    address = db.Column(db.String, unique = True, nullable = False)
    pincode = db.Column(db.Integer, unique = True, nullable = False)

class Admin(db.Model):
    __tablename__ = "admin"
    user_id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String, nullable = False)
    fullname = db.Column(db.String, unique = True, nullable = False)

class Parking_lot(db.Model):
    __tablename__ = "parking_lot"
    user_id = db.Column(db.Integer, primary_key = True)
    prime_location_name = db.Column(db.String, unique = True, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String, unique = True, nullable = False)
    pincode = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    fullname = db.Column(db.String, unique = True, nullable = False)

class Parking_spot(db.Model):
    __tablename__ = "parking_spot"
    user_id = db.Column(db.Integer, primary_key = True)
    prime_location_name = db.Column(db.String, unique = True, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String, unique = True, nullable = False)
    pincode = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    fullname = db.Column(db.String, unique = True, nullable = False)

class Reverse_parking_spot(db.Model):
    __tablename__ = "reverse_parking_spot"
    user_id = db.Column(db.Integer, primary_key = True)
    prime_location_name = db.Column(db.String, unique = True, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String, unique = True, nullable = False)
    pincode = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    fullname = db.Column(db.String, unique = True, nullable = False) 