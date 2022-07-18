from flask import Flask, flash, redirect, render_template, request, send_from_directory, jsonify
from application.database import db, User, Submission
from application.bot import visit_submission
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_session import Session
import hashlib
import time

app = Flask(__name__)

app.config.from_object('application.config.Config')

db.init_app(app)
db.create_all(app=app)

login_manager = LoginManager()
login_manager.init_app(app)
sess = Session()
sess.init_app(app)

flag = open("/flag.txt").read()

def response(message):
    return jsonify({'message': message})

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():

    ingredients = ["Ketchup","Mustard","Pickles","Onions","Tomato",
                   "American Cheese","Cheddar Cheese","Blue Cheese",
                   "Bacon","BBQ Sauce","Mayonaise","Rob's Secret Sauce",
                   "Ranch Dressing","Cucumber","Feta","Onion Ring",
                   "Fried Mac & Cheese","Tater Tots","Fried Egg","Hummus",
                   "Ham","Chicken Patty","Extra Burger Patty","Black Bean Burger",
                   "Fried Onions","Parsely","Marinara","Provolone","Mozzarella"]

    return render_template("index.html",ingredients=ingredients,logged_in=current_user.is_authenticated)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Access denied. You must be logged in.',"danger")
    return redirect('/')

@app.route('/login',methods=["POST"])
def login():

    username = request.form.get("username","").lower()
    password = request.form.get("password","")

    if not username or not password:
        flash('Incorrect username or password.',"danger")
        return redirect("/")

    password_hash = hashlib.sha256()
    password_hash.update(password.encode())

    user = User.query.filter_by(username=username,password=password_hash.hexdigest()).first()

    if user:
        login_user(user)
        flash('Login successful.',"success")
        return redirect("/")
    
    flash('Incorrect username or password.',"danger")
    return redirect("/")

@app.route('/register',methods=["POST"])
def register():

    username = request.form.get("username","").lower()
    password = request.form.get("password","")
    confirm_password = request.form.get("confirm_password","")

    if not username or not password or not confirm_password:
        flash('Missing required fields.',"danger")
        return redirect("/")

    user = User.query.filter_by(username=username).first()

    if user:
        flash('Username already exists.',"danger")
        return redirect("/")

    password_hash = hashlib.sha256()
    password_hash.update(password.encode())

    new_user = User(username=username,password=password_hash.hexdigest())
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    flash('Registration successful.',"success")
    return redirect("/")

@login_required
@app.route('/submission',methods=["POST"])
def new_submission():

    if not request.is_json:
        return response('Input must be JSON!'), 401

    data = request.get_json()

    app.logger.info(data)
    
    submission = Submission.query.filter_by(submitted_by=current_user.id, judged=False).order_by(Submission.date.desc()).first()
    
    if submission and submission.date.timestamp() + 10 > time.time():
        return response("You can only submit a burger once every 10 seconds. Please again in %d seconds." % (submission.date.timestamp() + 10 - time.time())), 401
    
    title = data.get('title','')
    recipe = data.get('recipe',[])
    comments = data.get('comments','')

    if not title:
        return response('Missing title!'), 401
    if not recipe:
        return response('Missing recipe!'), 401

    new_sub = Submission(title=title,submitted_by=current_user.id,recipe=",".join(recipe),comments=comments)
    db.session.add(new_sub)
    db.session.commit()

    # Ask bot to visit this submission
    visit_submission(new_sub.id)
    new_sub.judged = True
    db.session.commit()

    return response("Submission successful!"), 200

@app.route('/submission/<submission_id>',methods=["GET"])
def review_submission(submission_id):

    # Only allow review actions from bot on localhost
    local_conn = request.remote_addr == "127.0.0.1"

    if not local_conn and not current_user.is_authenticated:
        flash("You must be logged in to view submissions.","danger")
        return redirect("/")

    submission = Submission.query.filter_by(id=submission_id).first()

    if not submission:
        return render_template("404.html")

    if not local_conn and submission.submitted_by != current_user.id:
        flash("No peeking at others' burger recipes >:(","danger")
        return redirect("/")

    return render_template("submission.html",submission=submission,is_bot=local_conn,flag=flag)

@app.route('/submission/<submission_id>/approve',methods=["GET"])
def approve_submission(submission_id):

    # Only allow review actions from bot on localhost
    if request.remote_addr != "127.0.0.1":
        flash("Access Denied: Only the grillmaster can choose a winning burger recipe!","danger")
        return redirect("/")

    submission = Submission.query.filter_by(id=submission_id).first()

    if not submission:
        return render_template("404.html")

    submission.winner = True

    db.session.commit()

    return "Burger recipe approved!"

@app.route('/submissions',methods=["GET"])
@login_required
def submissions():
    submissions = Submission.query.filter(Submission.submitted_by==current_user.id).all()
    return render_template("submissions.html",submissions=submissions)