import os
import json
from flask import Flask
from parser import Parser

app = Flask(__name__)
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
def ask(user_id=None, sentence=None):
    return json.dumps(par.respond(user_id, sentence))

app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)))