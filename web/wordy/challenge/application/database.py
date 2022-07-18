from flask_sqlalchemy import SQLAlchemy
from flask import current_app
import random

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(50))
    word = db.Column(db.String(5))
    guessed_time = db.Column(db.Integer,default=0)