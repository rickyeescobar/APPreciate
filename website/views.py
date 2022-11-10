import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from flask import Blueprint

views = Blueprint("views", __name__)



@views.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@views.route('/', methods=["GET", "POST"])
def home():
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
