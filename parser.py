#from pymongo import MongoClient
from datetime import datetime, timedelta

class Parser:
	def __init__(self):
		self.waiters = {}
		self.match = {'players': [], 'startTime': None}

	def respond(self, user_id, sentence):
		self.initBasicResponse()
		
		if sentence.find('ping') > -1 or sentence.find('pong') > -1:
			self.badSpelling()
		
		if sentence.find('jugar') > -1 and sentence.find('ping') > -1 and sentence.find('pong') > -1:
			self.newPlayer(user_id)
			
		if sentence.find('si') > -1 and user_id in self.waiters:
			self.confirmation(user_id)
		
		return self.response
	
	def confirmation(self, user_id):
		self.match['players'].append(user_id)
	
	def sync(self, user_id):
		self.response = {
			'msg' : '',
			'stillSync' : True,
			'users_ids' : []
		}
		
		if user_id in self.waiters and len(self.waiters) > 1:
			self.response['msg'] = 'Ya hay nuevos ineteresados.\n'
			self.askForWaiters()
			self.response['stillSync'] = False
		
		return self.response
	
	def badSpelling(self):
		self.response['msg'] = 'Quisiste decir ping pong?'
	
	def  newPlayer(self, user_id):
		print self.waiters
		self.waiters[user_id] = datetime.utcnow()
		
		self.response['understand'] = True
		self.response['waitResponce'] = True
		self.response['cacheTime'] = 0
		
		self.askForWaiters()
	
	def askForWaiters(self):
		self.response['msg'] += 'Queres jugar con'
		for user, time in self.waiters.iteritems():
			if user not in self.response["users_ids"]:
				self.response["users_ids"].append(user)
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
	