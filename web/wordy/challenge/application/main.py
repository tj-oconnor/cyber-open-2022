from flask import Flask, render_template, request, jsonify ,make_response
from application.database import db,Game
import uuid
import random
import os
import time
import json

app = Flask(__name__)
app.secret_key = os.urandom(15)

app.config.from_object('application.config.Config')

db.init_app(app)
db.create_all(app=app)

flag = open("/flag.txt").read()
words = json.loads(open("/words.json","r").read())

dw_tag = "<p>Having fun? <a href='https://grnh.se/82dc5d093us' target='_blank'>We're hiring!</a> &#128058;<br></p>"

@app.route('/')
def index():

    resp = render_template("index.html")

    return resp

@app.route('/api/game',methods=["GET"])
def newgame():
    new_game_id = str(uuid.uuid4())
    new_game = Game(game_id=new_game_id,word=random.choice(words))
    db.session.add(new_game)
    db.session.commit()
    return jsonify({'game_id':new_game.game_id}), 200

@app.route('/api/guess',methods=["POST"])
def guess():

    if not request.is_json:
        return jsonify({'error': 'Input must be JSON'}), 401

    data = request.get_json()

    game_id = data.get('game_id','')
    guess = data.get('guess','')

    if not game_id:
        return jsonify({'error': 'Missing game ID.'}), 401
    if not guess:
        return jsonify({'error': 'Missing guess.'}), 401
    if len(guess) != 5:
        return jsonify({'error': 'Guess must be 5 characters.'}), 401

    game = Game.query.filter_by(game_id=game_id).first()

    if not game:
        return jsonify({'error': 'Expired or invalid game ID. Games are deleted 5 seconds after your guess to reduce memory usage.'}), 401

    if game.guessed_time != 0 and game.guessed_time + 5 < time.time():
        db.session.delete(game)
        db.session.commit()
        return jsonify({'error': 'Expired or invalid game ID. Games are deleted 5 seconds after your guess to reduce memory usage.'}), 401

    # Mark game as completed for deletion
    game.guessed_time = time.time()
    db.session.commit()


    new_game_id = str(uuid.uuid4())
    new_game = Game(game_id=new_game_id,word=random.choice(words))
    db.session.add(new_game)
    db.session.commit()

    if guess.lower() == game.word:
        resp = make_response(jsonify({'message': 'Correct! You guessed "%s"!<br><br>And now for your prize! Use the code below for a free subscription to Wordy when we implement a $29.99/month fee soon!<br><br><b>Discount Code: %s</b>%s' % (guess.lower(),flag,dw_tag),
                                      'correct_word':game.word,
                                      'game_id':new_game.game_id}), 200)
    else:
        resp = make_response(jsonify({'message': 'Incorrect! Sorry, the correct word was "%s"' % game.word,
                                      'correct_word':game.word,
                                      'game_id':new_game.game_id}), 200)


    return resp