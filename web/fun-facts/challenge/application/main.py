from flask import Flask, render_template, request, jsonify
from application.database import db, Subscription
import json
import os
from pywebpush import webpush
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = os.urandom(15)

app.config.from_object('application.config.Config')

db.init_app(app)
db.create_all(app=app)

flag = open("/flag.txt").read()
vapid = json.loads(open("/vapid.json").read())

app.logger.info(vapid)

def response(message):
    return jsonify({'message': message})

@app.route('/')
def index():
    return render_template("index.html",publicKey = vapid["publicKey"])

@app.route('/api/register',methods=["POST"])
def api_register():

    if not request.is_json:
        return response('Input must be JSON'), 401

    data = request.get_json()

    if "endpoint" not in data:
        return response('Missing required "endpoint" field.'), 401
    if "keys" not in data:
        return response('Missing required "keys" field.'), 401

    newsub = Subscription(sub_info=request.get_data())
    db.session.add(newsub)
    db.session.commit()
    return response('Subscription complete.'), 200

def send_facts():

    flag_text = "Great job! You get a special prize, the flag: %s" % flag

    with app.app_context():
    
        subs = Subscription.query.all()

        # Send all subscriptions the flag and hopefully they'll get it
        for sub in subs:
            try:
                webpush(json.loads(sub.sub_info),flag_text,vapid_private_key=vapid["privateKey"],vapid_claims={"sub": "mailto:jacob@jseis.me"})
            except Exception as e:
                app.logger.info("Push Exception: %s" % str(e))

# Send flags every minute to anyone who successfully subscribed.
scheduler = BackgroundScheduler()
scheduler.add_job(func=send_facts, trigger="interval", seconds=60)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())