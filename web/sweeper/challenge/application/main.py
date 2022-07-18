from flask import Flask, render_template, request, jsonify, redirect
from flask_sock import Sock
import json
import random
import traceback
from application.sweeper import Sweeper
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config.from_object('application.config.Config')

sock = Sock(app)

flag = open("/flag.txt").read()

def response(message_type,message):
    return json.dumps({"message_type":message_type,"message": message})

def modal(title,body):
    return response("modal",{"title":title,"body":body})

@app.route('/')
def index():
    return render_template("index.html")

@sock.route('/game')
def game_ws(sock):

    sock.send(modal("Welcome to Sweeper!","Clear all the mines to win a fabulous prize. Right-click to flag mines if you know where they are."))

    # Start new game for each socket connection
    game = Sweeper(app.config["GAME_WIDTH"],app.config["GAME_HEIGHT"],app.config["GAME_RATIO"])
    sock.send(response("game_config",{"width":app.config["GAME_WIDTH"],"height":app.config["GAME_HEIGHT"]}))
    sock.send(response("message","New game started."))
    sock.send(response("game_state",game.get_game_state()))

    while True:
        data = sock.receive()
        try:
            app.logger.info("Game Input: %s" % (data))
            game_input = json.loads(data)
        except ValueError:
            app.logger.info("Invalid input, must be JSON")
            sock.send(response("error","Invalid input, must be JSON."))
            continue
        except ConnectionError:
            app.logger.info("Client disconnected.")
            break

        message_type = game_input.get("message_type","")

        if not message_type:
            app.logger.info("Invalid input, no action specified")
            sock.send(response("error","Invalid input, no action specified."))

        if message_type == "reset":
            # Create new game object
            
            app.logger.info("Reset Game")
            game = Sweeper(app.config["GAME_WIDTH"],app.config["GAME_HEIGHT"],app.config["GAME_RATIO"])
            sock.send(response("message","New game started."))
            
            app.logger.info("New game started")
            sock.send(response("game_state",game.get_game_state()))
        
        elif message_type == "ping":
            sock.send(response("pong",""))

        elif message_type == "click":

            x = game_input.get("x",None)
            y = game_input.get("y",None)

            if x is None or y is None:
                app.logger.info("Invalid input, No coordicates in click event")
                sock.send(response("error","No coordinates in click event."))
                continue
            
            if (x < 0 or x >= game.width) or (y < 0 or y >= game.height):
                sock.send(response("error","Click event coordinates out of bounds."))
                continue

            # Send click event to game
            game.click_space(x,y)
            sock.send(response("game_state",game.get_game_state()))

        elif message_type == "flag":

            x = game_input.get("x",None)
            y = game_input.get("y",None)

            if x is None or y is None:
                sock.send(response("error","No coordinates in click event."))
                continue
            
            if (x < 0 or x >= game.width) or (y < 0 or y >= game.height):
                sock.send(response("error","Click event coordinates out of bounds."))
                continue

            # Send click event to game
            game.flag_space(x,y)
            sock.send(response("game_state",game.get_game_state()))

        elif message_type == "save":
            sock.send(response("save",game.dump_state()))

        elif message_type == "load":

            state = game_input.get("state",None)

            if state is None:
               sock.send(response("error","No game state provided."))
            
            try:
                game.load_state(state)
                sock.send(response("message","Loaded game ID: %s" % game.game_id))
                sock.send(response("game_state",game.get_game_state()))
            except Exception as e:
                sock.send(response("error",str(e)))

        if game.game_over and game.winner:
            sock.send(modal("Good Job!","You cleared all the mines so you get a prize in the form of a tip. The flag is located on my server at /flag.txt"))
        elif game.game_over and not game.winner:
            sock.send(modal("Kaboom!","Better luck next time. Click the reset button to try again..."))
    
        
        
        
    



