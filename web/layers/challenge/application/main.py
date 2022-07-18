from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    with open("/app/service_dir/hostname","r") as F:
        return render_template("index.html")


@app.route('/join')
def join_us():

    # If the connection is coming from 127.0.0.1 then it is being routed from Tor
    if request.remote_addr == "127.0.0.1":
        with open("/app/flag.txt","r") as F:
            return render_template("flag.html",flag=F.read())

    # Else try again
    with open("/app/service_dir/hostname","r") as F:
        return render_template("join.html",onion_link=F.read().replace(".onion",""))