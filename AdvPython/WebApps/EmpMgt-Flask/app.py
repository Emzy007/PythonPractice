from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return "<a href=""> Some </a>"

@app.route("/emp")
def mypage():
    return "<h1>Emp Mgt Sys2 using Flask</h1>"

