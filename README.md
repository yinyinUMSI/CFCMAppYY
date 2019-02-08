# CFCM Skeleton App

This is a skeleton web application using the MongoDB, Flask, backbone.js,
bootstrap.js stack.  You can use it as a starting point to create your own
web app based on this stack.

## Contents
* [Installation](#installation)
* [Forking](#forking)
* [Setup](#setup)
* [Running](#running)


## Installing
To create your own application based on this one, first create a new git
repository (e.g. on github).  Next, clone this repo:

    $ git clone https://github.com/elplatt/Flask-Backbone-Skeleton.git MyApp
    

## Forking
If you would like to create a repository for your new app, first create an empty git repository.
Then change the origin on the cloned repo to the repo for your new app,
and push.

    $ cd MyApp
    $ git remote rm origin
    $ git remote add origin https://github.com/myuser/MyApp.git
    $ git push -u origin master

This example will push a fresh fork of the repo to `myuser`'s `MyApp` repo.

## Installation
To install this app, first install the dependencies, and then create a
configuration file.

### Dependencies

pip install requirements.txt

## Running

To run the app locally, just run `server.py`:

    $ python server.py

