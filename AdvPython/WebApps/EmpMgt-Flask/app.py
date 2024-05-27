from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy #Added 27-May-2024
import os #Added 27-May-2024

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empskills.db'

db = SQLAlchemy(app)

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailid = db.Column(db.String(250))
    skills = db.Column(db.Text())

if not os.path.isfile('empskills.db'):
    db.create_all()

@app.route("/")
def homepage():
    return "<a href=""> Some </a>"

@app.route("/test")
#complete URL - https://vigilant-sniffle-x55gqw4r5q4qh6vp5-5000.app.github.dev/emp
def test():
    return "<h1>Emp Mgt Sys2 using Flask</h1>"

@app.route("/skillset/update", methods = ['GET', 'POST'])
def updateskillset():
    if request.method == 'POST':
        email = request.form['email']
        skillset = ",".join(request.form.getlist('skills'))
        data = Skills(emailid = email, skills = skillset)
        db.session.add(data)
        db.session.commit()
        return render_template('updateskill.html', success = 'Skill set updated successfully')
    return render_template('updateskill.html')