# Gabriel Summers

import random

class Player:
	def __init__(self):
		self.name = 'prisoner'
		self.items = ['health potion', 'bomb']
		self.health = 10
		self.weapon = 'dagger'
		self.armor = 8

	def printAll(self):
		desc =  ''.join(['My name is ',\
					   	 self.name,\
					     '.\nI am weilding a ',\
					     self.weapon,\
					     '.\nI have ',\
					     str(self.health),\
					     ' health left and ',\
					     str(self.armor),\
					     ' armor.\nI have ',\
					     str(len(self.items)),\
					     ' items.\n'])
		print desc
		if len(self.items) > 0:
			print 'They are: ', self.items



myself = Player() 

monsters 	= 	['spider','troll','bandit','slime','skeleton','zombie','goblin']
monDesc 	= 	['hairy','aggressive','large','smelly','rotted','evil','angry',\
		   	 	 'confused','scary','badass','hungry','fancy']
roomDesc	= 	['cold','empty','bright','cluttered','warm','stinky','fancy',\
				 'dark']
roomLocation=	['floor','table','rug']
roomItem	=	['chest','sword','bag of gold','gem','scroll','book','mask']

def generateTxt():
	output = ''.join(['\nYou enter the ',\
					 random.choice(roomDesc),\
					 ' room and see a ',\
					 random.choice(roomItem),\
					 ' on the ',\
					 random.choice(roomLocation),\
					 '.\nIn the corner you see a ',
					 random.choice(monDesc),
					 ' ',
					 random.choice(monsters),
					 '\n\n... What do you do?\n\n'])
	print output

def start():
	myself.printAll()



generateTxt()
start()