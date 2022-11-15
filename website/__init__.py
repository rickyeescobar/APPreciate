import os
from flask import Flask
from flask_session import Session



def create_app(test_config=None):
    # configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'website.sqlite'),
        # Ensure templates are auto-reloaded
        TEMPLATES_AUTO_RELOAD = True,
        # Configure session to use filesystem (instead of signed cookies)
        SESSION_PERMANENT = False,
        SESSION_TYPE = "filesystem")

    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
   
    from .auth import auth 
    app.register_blueprint(auth)

    from .community import community
    app.register_blueprint(community)
    
    from .views import views
    app.register_blueprint(views)
    app.add_url_rule('/',endpoint='index')


    from . import db
    db.init_app(app)

    # session
    Session().init_app(app)



    return app