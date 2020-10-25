from flask_login import UserMixin
from ..app import db

# database model to represent Users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    major = db.Column(db.String(1000))
    year = db.Column(db.Integer)
    class1 = db.Column(db.String(100))
    class2 = db.Column(db.String(100))
    class3 = db.Column(db.String(100))
    class4 = db.Column(db.String(100))
    class5 = db.Column(db.String(100))
    class6 = db.Column(db.String(100))
    interests = db.Column(db.String(1000))