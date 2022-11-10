import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# configure app
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True  

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        
        phrase = request.form.get("phrase")
        
        sid = SentimentIntensityAnalyzer()
        analyzed = sid.polarity_scores(phrase)

        if analyzed["compound"] > 0:
            phrase = ":)"
        elif analyzed["compound"] == 0:
            phrase = ":|"
        else:
            phrase = ":("



       
      

        return render_template("index.html", analyzed=analyzed, phrase=phrase)

    else:
        return render_template("index.html")

