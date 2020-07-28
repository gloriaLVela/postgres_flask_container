from flask import Flask
import flask_sqlalchemy

from models import db
# from . import config
import config


def create_app():
    #  Create an app called flask_app
    flask_app = Flask(__name__)
    flask_app.config.from_object('config')
    # Assign the URI from the config file to the Flask app's configuration. 
    # This URI is used to connect to the Postgres database
    flask_app.config['SQL_ALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # We are using Flask contexts. Since Flask can have nultiple apps we have to specify 
    # which app we are using with SLQAlchemy
    flask_app.app_context().push()
    # Link the db to the Flask app
    db.init_app(flask_app)
    # Create the database tables, if they do not exist
    db.create_all()
    return flask_app