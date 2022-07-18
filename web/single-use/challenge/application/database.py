from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from flask_login import UserMixin
import random

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    code = db.Column(db.String(4))


class Banlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    attempts = db.Column(db.Integer,default=0)
    attempt_time = db.Column(db.Integer)