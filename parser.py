#from pymongo import MongoClient
from datetime import datetime, timedelta

class Parser:
	def __init__(self):
		self.waiters = []
		#self.mclient = MongoClient()
		#self.mdb = self.mclient.pingpong_manager
	
	def badSpelling(self):
		self.response['msg'] = 'Quisiste decir ping pong?'
	
	def  newPlayer(self, user_id):
		self.waiters.append({
				"user_id" : user_id,
				"time" : datetime.utcnow()
			})
		
		self.response['msg'] = 'Queres jugar con'
		self.response['understand'] = True
		self.response['waitResponce'] = True
		self.response['cacheTime'] = 0
		
		for user in self.waiters:
			if user['user_id'] not in self.response["users_ids"]:
				self.response["users_ids"].append(user['user_id'])
				self.response['msg'] += ' %us_id'
		
		self.response['msg'] += '?'
	
	def initBasicResponse(self):
		self.response = {
			'msg' : 'No entiendo',
			'waitResponce' : False,
			'understand' : False,
			'cacheTime' : 10000,
			'users_ids' : []
		}
	
	def respond(self, user_id, sentence):
		self.initBasicResponse()
		
		if sentence.find('ping') > -1 or sentence.find('pong') > -1:
			self.badSpelling()
		
		if sentence.find('jugar') > -1 and sentence.find('ping') > -1 and sentence.find('pong') > -1:
			self.newPlayer(user_id)
		
		return self.response