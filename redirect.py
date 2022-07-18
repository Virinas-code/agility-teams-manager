import os
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect("https://agilityteamsmanager.pythonanywhere.com", code=302)
