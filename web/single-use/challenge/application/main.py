from flask import Flask, render_template, request, jsonify, redirect
from application.database import db, User, Banlist
import json
import os
import random
import time
from pyotp import TOTP
import base64
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_session import Session
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

db.init_app(app)
db.create_all(app=app)
login_manager = LoginManager()
login_manager.init_app(app)
sess = Session()
sess.init_app(app)

flag = open("/flag.txt").read()

# Add company users with random OTP codes (using fairly low numbers because I don't wanna be TOO mean)
with app.app_context():

    #Clear DB first
    db.session.query(User).delete()
    db.session.commit()

    db.session.add(User(username="admin",first_name="Stephen",last_name="Johnson",code=str(random.randint(100,200)).zfill(4)))
    db.session.add(User(username="bjones",first_name="Brandon",last_name="Jones",code=str(random.randint(0,100)).zfill(4)))
    db.session.add(User(username="hlivingston",first_name="Heather",last_name="Livingston",code=str(random.randint(0,100)).zfill(4)))
    db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def response(message):
    return jsonify({'message': message})

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
@login_required
def dashboard():

    otp_code = current_user.code
    otp_seed = base64.b32encode(otp_code.zfill(10).encode())

    uri = TOTP(otp_seed).provisioning_uri(name=current_user.username, issuer_name='USCG Single-Use')
    return render_template("dashboard.html",user=current_user,otp_uri=uri,otp_code=otp_code,otp_seed=otp_seed.decode(),flag=flag)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/api/register',methods=["POST"])
def api_register():

    if not request.is_json:
        return response('Input must be JSON'), 401

    data = request.get_json()

    username = data.get("username",False).lower()
    first_name = data.get("first_name",False)
    last_name = data.get("last_name",False)

    if not username or not first_name or not last_name:
        return response('Missing required fields.'), 401

    existing = User.query.filter_by(username=username).first()

    if existing:
        return response('Username already exists.'), 401

    new_user = User(username=username,first_name=first_name,last_name=last_name,code=str(random.randint(0,9999)).zfill(4))
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return response('Registration successful.'), 200

@app.route('/api/login',methods=["POST"])
def api_login():

    if not request.is_json:
        return response('Input must be JSON'), 401

    data = request.get_json()

    username = data.get("username","").lower()
    code = data.get("code","")

    if not username or not code:
        return response('Missing required fields.'), 401

    user = User.query.filter_by(username=username).first()
    user_ip = request.headers.getlist("X-Forwarded-For")[0] 
    app.logger.info("username: %s IP: %s" % (username, user_ip))

    if is_banned(user_ip):
        return response('Your IP address is currently locked out. Please try again later.'), 400
    
    ban_count = ban_attempts(request.remote_addr)
    app.logger.info("username: %s IP: %s, Ban attempts: %s" % (username, user_ip, ban_count))

    if user:

        test_code = TOTP(base64.b32encode(user.code.zfill(10).encode())).now()

        app.logger.info("TOTP Codes: Input = %s, User = %s" % (code,test_code))

        if test_code == code:
            clear_ban(request.remote_addr)
            login_user(user)
            return response('Login successful.'), 200

        if ban_count == 9:
            return response('Username or password is incorrect. IP address locked out for 5 minutes.'), 400
    
    return response('Username or password is incorrect. You have %d attempts remaining before being locked out.' % (10 - ban_count)), 400

def ban_attempts(ip):

    ban = Banlist.query.filter_by(ip=ip).first()
    
    if not ban:
        ban = Banlist(ip=ip,attempts=1,attempt_time=time.time())
        db.session.add(ban)
        db.session.commit()
        return 1
    
    ban.attempts += 1
    ban.attempt_time = time.time()
    db.session.commit()
    app.logger.info("Attempts: %s IP: %s, Time: %s" % (ban.attempts, ban.ip, ban.attempt_time))
    
    return ban.attempts

def is_banned(ip):

    ban = Banlist.query.filter_by(ip=ip).first()

    if ban:
        if ban.attempts >= 9 and ban.attempt_time + 300 > time.time():
            return True
        elif ban.attempts >= 9 and ban.attempt_time + 300 < time.time():
            db.session.delete(ban)
            db.session.commit()
    return False

def clear_ban(ip):

    ban = Banlist.query.filter_by(ip=ip).first()
    if ban:
        db.session.delete(ban)
        db.session.commit()
    
        
        
        
    



