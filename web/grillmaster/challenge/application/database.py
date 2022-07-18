from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import current_app
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(64))

    def is_authenticated():
        return True

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitted_by = db.Column(db.Integer)
    title = db.Column(db.String(250))
    recipe = db.Column(db.String(500))
    comments = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    winner = db.Column(db.Boolean,default=False)
    judged = db.Column(db.Boolean, default=False)
