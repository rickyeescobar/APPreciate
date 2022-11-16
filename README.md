# APPreciate

## files
1. app.py
2. README.md
3. requirements.txt
4. setup.py
5. MANIFEST.in
4. website
    * static
        * favicon.ico
        * styles.css
    * templates
        * auth
            * login.html
            * sign_up.html
        * community
            * create_community.html
            * join_community.html
            * my_community.html
        * views
            * create.html
            * functionality.html
            * index.html
            * update.html
        * layout.html
    * '__init__.py'
    * auth.py
    * community.py
    * views.py
    * db.py
    * schema.sql


#### Video Demo: TODO
#### Developer's name:
>##### Ricky Escobar
#### City:
>##### Houston, Texas
#### Country:
>##### United States

#### Description:
###### APPreciate is a social network style app. It's goal is to increase workplace and school productivity as well as improve relationships and the mental health of its users. APPreciate is a web app built on Flask, inspired by Dale Carnegie's "How to Win Friends and Influence People. The goal of the App is to increase workplace and classroom productivity and quality of work by promoting positive reinforcement for users. Users can only post things with a positive sentiment score. Users can join "communities" that could be workplace teams, classrooms, companies, schools, or even groups of friends. Users can see posts made in the communities they are a part of. APPreciate fixes the problem of toxic social media interactions and comparison by biasing for positive "appreciation" posts about people. Company productivity will increase because people are more likely to do a better job if they are being praised for their work, and they are eager to receive praise. 


### Required Libraries:
>- import os
>- from flask import Flask, Blueprint, flash, redirect, render_template, request, session, url_for
>- from flask_session import Session
>- import functools
>- from nltk.sentiment.vader import SentimentIntensityAnalyzer
>- from werkzeug.security import check_password_hash, generate_password_hash
>- import click
>- import setuptools
>- from werkzeug.exceptions import abort



### Description of functionality:
#### __init__.py 
###### Sets up app configuration, tests if app is ready to run, registers blueprints, returns app.

#### app.py
###### Runs code from __init__.py and creates the Flask app instance.

#### db.py
###### Initiates and controls the SQLite database interface. Contains the functions: get_db(), close_db(), init_db('init-db'), init_db_command(), and init_app(app). These functions allow the flask app to interact with the SQLite backend for all basic website functinality. 

#### schema.sql
######
DROP TABLE IF EXISTS user;

DROP TABLE IF EXISTS post;

DROP TABLE IF EXISTS community;

DROP TABLE IF EXISTS community_user;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  body TEXT NOT NULL,
  community_name TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id),
  FOREIGN KEY (community_name) REFERENCES community (name)
);

CREATE TABLE community (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT  NOT NULL UNIQUE,
  owner_id INTEGER NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES user (id)
);

CREATE TABLE community_user (
  user_id INTEGER NOT NULL,
  community_name TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (community_name) REFERENCES community (name)

);

#### auth.py
###### Allows for user authentication. Contains the functions: sign-up(), login(), load_logged_in_user(), logout(), and login_required(view). This file manages all of the routes for user authentication functionality such as logging in, signing up, logging out, etc. 

#### views.py
###### Allows for central functionality of the app, the sentiment-based input regulation. Contains the functions: test_sentiment(phrase), after_request(response), index(), create(), functionality(), get_post(), update(id), and delete(id). This file manages the routes for the base functionality of the app. It ensures that users can only submit posts to communities that contain a positive sentiment score. The minimum sentiment score allowed can also be adjusted with the variable SENTIMENT_MIN. The functionality utilizes the SentimentIntensityAnalyzer from NLTK (nltk.sentiment.vader). This file allows users to create posts, update posts, or delete posts, so long as they follow the sentiment guidelines. It also provides functionality for the "functionality" page on the website that acts as a demo for the app.

#### community.py
###### Allows users to create, join, delete, or leave communities of other users. Contains the functions my_community(), create_community(), join_community(), get_community_user(community_name), get_community(name), leave_community(community_name), and delete_community(community). This file manages the community functionality for the web app. It allows users to create communities that could be groups of peers, entire companies, schools, classes, or any group of people you want. Communities have an owner (the creator of the group) who is the only one who can delete the group. After joining an existing group, you may leave a group. Any user can create a group or join other groups. Users can join many groups at the same time. On the app's home page, users will see a feed of all posts within their groups. From the my community link in the nav bar, users can access the functionality of this file. 




# TODO
# Thanks for reading
