
import configparser

import flask

# Load configuration
config = configparser.ConfigParser()
config.read('app.config')

# Flask app
app = flask.Flask(__name__)
app.secret_key = 'put secret key here'

# Set up routes and content
from app import views
