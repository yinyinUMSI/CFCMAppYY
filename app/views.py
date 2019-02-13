import json

import flask
from flask import request

from app import app
from app.forms import *

@app.route('/')
def index():
    content = '<p>To add content, modify <code>views.py</code>.<p>'
    return flask.render_template('main.html', content=content)

@app.route('/comments/')
def commentPage():
    content = '<p>Hello I\'m comment page.<p>'
    return flask.render_template('comments.html', content=content)

@app.route('/commentsResult/')
def commentResult():
	if request.method == 'GET':

	    content = request.args.get('inputText')
	    return flask.render_template('comments.html', content=content)

