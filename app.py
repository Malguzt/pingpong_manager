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
    response = _getBasicResponse()
    
    if sentence.find('ping') > -1 or sentence.find('pong') > -1:
        response['msg'] = 'Quisiste decir ping pong?'
        response['cacheTime'] = 10000
        
    if sentence.find('jugar') > -1 and sentence.find('ping') > -1 and sentence.find('pong') > -1:
        response['msg'] = 'Queres jugar con esta?'
        response['understand'] = True
        response['waitResponce'] = True
    
    return json.dumps(response)

def _getBasicResponse():
    return {
        'msg' : 'No entiendo',
        'waitResponce' : False,
        'understand' : False,
        'cacheTime' : 0
        }

app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)))