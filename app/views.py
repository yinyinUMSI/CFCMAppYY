import json

import flask

from app import app
from app.forms import *

@app.route('/')
def index():
    content = '<p>To add content, modify <code>views.py</code>.<p>'
    return flask.render_template('main.html', content=content)

@app.route('/comments')
def datafunction():
    return "hello"
    
