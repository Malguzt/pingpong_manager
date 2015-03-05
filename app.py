import os
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    endpoints = {
        'endpoints' : {
            '/keywords' : ['GET'],
            '/sentence/<sentence>' : ['GET']
            }
        }
    return json.dumps(endpoints)

@app.route('/keywords/', methods=['GET'])
def keywords():
    wordsList = {"ping" : 5, "pong" : 5, "pingpong" : 10}
    return json.dumps(wordsList)

@app.route('/sentence/<sentence>', methods=['GET'])
def ask(sentence=None):
    respond = {
        'msg' : 'No entiendo',
        'waitResponce' : False,
        'understand' : False,
        'cacheTime' : 0
        }
    
    if sentence.find('ping') > -1 or sentence.find('pong') > -1:
        respond['msg'] = 'Quisiste decir ping pong?'
        respond['cacheTime'] = 10000
        
    if sentence.find('jugar') > -1 and sentence.find('ping') > -1 and sentence.find('pong') > -1:
        respond['msg'] = 'Queres jugar con esta?'
        respond['understand'] = True
        respond['waitResponce'] = True
    
    return json.dumps(respond)

app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)))