import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
import json
from parser import Parser


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
par = Parser()

@app.route('/')
def root():
    endpoints = {
        'endpoints' : {
            '/keywords' : ['GET'],
            '/sentence/<user_id>/<sentence>' : ['GET']
            }
        }
    return json.dumps(endpoints)

@app.route('/keywords/', methods=['GET'])
def keywords():
    wordsList = {"ping" : 5, "pong" : 5, "pingpong" : 10}
    return json.dumps(wordsList)

@app.route('/sentence/<user_id>/<sentence>', methods=['GET'])
def sentence(user_id=None, sentence=None):
    return json.dumps(par.respond(user_id, sentence))

@app.route('/sync/<user_id>', methods=['GET'])
def sync(user_id=None, sentence=None):
    return json.dumps(par.sync(user_id))

if __name__ == '__main__':
    app.run()
