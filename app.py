from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database("database.db")

@app.route("/")
def index():
    ews = db.get_ews()
    return render_template("list.html", ews=ews)

@app.route("/add", methods=["POST"])
def add_ew():
    task = request.form["task"]
    subject = request.form["subject"]
    beak = request.form["beak"]
    due_date = request.form["due_date"]
    db.create_ew(task, subject, beak, due_date)
    return redirect("/")
