from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from website import create_app

# configure app
app = create_app()

Session(app)


