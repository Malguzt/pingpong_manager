from pymongo import MongoClient
from datetime import datetime, timedelta

class Parser:
    def __init__(self, user_id, sentence):
        self.mclient = MongoClient()
        self.mdb = self.mclient.pingpong_manager
        self.user_id = user_id
        self.sentence = sentence
    
    def respond(self):
        self.__initBasicResponse()
        
        if self.sentence.find('ping') > -1 or self.sentence.find('pong') > -1:
            self.__badSpelling()
        
        if self.sentence.find('jugar') > -1 and self.sentence.find('ping') > -1 and self.sentence.find('pong') > -1:
            self.__newPlayer()
        
        return self.response
    
    def __badSpelling(self):
        self.response['msg'] = 'Quisiste decir ping pong?'
    
    def  __newPlayer(self):
        waiters = self.mdb.waiting_list
        showTime = datetime.utcnow()
        
        newWaiter = {
                "user_id" : self.user_id,
                "time" : showTime
            }
        
        waiters.insert(newWaiter)
        self.response['msg'] = 'Queres jugar con'
        self.response['understand'] = True
        self.response['waitResponce'] = True
        self.response['cacheTime'] = 0
        
        self.response["users_ids"] = []
        for user in waiters.find({'time' : {'$gte' : showTime - timedelta(hours=8)}}):
            if user['user_id'] not in self.response["users_ids"]:
                self.response["users_ids"].append(user['user_id'])
                self.response['msg'] += ' %us_id'
        
        self.response['msg'] += '?'
    
    def __initBasicResponse(self):
        self.response = {
            'msg' : 'No entiendo',
            'waitResponce' : False,
            'understand' : False,
            'cacheTime' : 10000
        }