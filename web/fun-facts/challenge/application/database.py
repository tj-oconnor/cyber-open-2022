from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import current_app

db = SQLAlchemy()

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_info = db.Column(db.String(1000))

