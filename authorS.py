from random import choice, randrange

table = [('a dead body','NN'),('a burnt corpse','NN'),('large','JJ'),('small','JJ'),\
		('hot','JJ'),('freezing','JJ'),('friged','JJ'),('dark','JJ'),\
		('bright','JJ'),('a sword','NN'),('a potion','NN'),('a helmet','NN'),\
		('a pair of pants','NN'),('a shirt','NN'),('some armor','NN'),\
		('a blade','NN'),('a scroll','NN'),('gold','NN'),('ancient','JJ'),\
		('a knife','NN'),('a hammer','NN'),('in','PR'),\
		('on','PR'),('under','PR'),('on top of','PR'),('inside of','PR'),\
		('next to','PR'),('beside','PR'),('near','PR'),('table','NO'),\
		('bench','NO'),('chest','NO'),('workbench','NO'),('rack on the wall','NO'),\
		('quiet','JJ'),('crate','NO'),('a gem','NN'),('some gold','NN'),\
		('burnt','JJ'),('scorched','JJ'),('dirty','JJ'),('a pile of bones','NN'),\
		('a blood-stain','NN'),('some ash','NN'),('a skeleton','MN'),('an ogre','MN'),\
		('a bandit','MN'),('a vampire','MN'),('a zombie','MN'),('a stone gollum','MN'),\
		('a goblin','MN'),('an orc','MN')]

collect=['a sword','a potion','a helmet','a pair of pants','a shirt',\
		'some armor','a blade','a knife','a hammer','a gem','some gold']

items=['a potion','a gem','some gold']

weapons={'a sword':13,'a blade':9,'a knife':6,'a hammer':10,'a stick':2}

armors={'a helmet':5,'a pair of pants':3,'a shirt':8,'some armor':13,'rags':1}

monsters={'a skeleton':5,'an ogre':25,'a bandit':6,'a vampire':15,\
			'a zombie':10,'a stone gollum':30,'a goblin':3,'an orc':20}

adjL = [word for word, pos in table\
		if pos.startswith('JJ')]
nounL =[word for word, pos in table\
		if pos.startswith('NN')]
destL =[word for word, pos in table\
		if pos.startswith('NO')]
prepL =[word for word, pos in table\
		if pos.startswith('PR')]
monsL =[word for word, pos in table\
		if pos.startswith('MN')]
item = None
desc = None
mons = None
health = 100
inventory = ['rags', 'a stick', 'a potion', 'a potion']
weapon = 'a stick'
armor = 'rags'

def generateRoomOp1():
	global item, desc, mons
	desc = choice(adjL)
	adje = choice(adjL)
	item = choice(nounL)
	prep = choice(prepL)
	obje = choice(destL)
	mons = None
	print ('\t\tYou enter the',desc,'room and see',item,'that looks',\
			adje,prep,'a',obje,'.')

def generateRoomOp2():
	global item, desc, mons
	desc = choice(adjL)
	item = None
	mons = None
	print ('\t\tYou enter a',desc,'room.')

def generateRoomOp3():
	global item, desc, mons
	desc = choice(adjL)
	item = None
	moch = choice(monsL)
	mons = (moch, monsters[moch])
	print ('\t\tYou enter a',desc,'room and see',mons[0],'about to attack!')


def generateRoom():
	num = randrange(3)
	if num == 0:
		generateRoomOp1()
	elif num == 1:
		generateRoomOp2()
	else:
		generateRoomOp3()

def showRoom():
	if desc is not None:
		if item is not None:
			print('\t\tThe room is',desc,'... There is',item,'in the room.')
		if mons is not None:
			print('\t\tThe room is',desc,'... There is',mons[0],'about to attack!')
		else:
			print('\t\tThe room is',desc)
	else:
		print('\t\tYou have not generated a room yet.')

def fight():
	global mons, health
	if randrange(10) < 7:
		print('\t\t\t\t',mons[0],'has',mons[1],'health..')
		mons = (mons[0],mons[1]-weapons[weapon])
		print('\t\t\t\tYou swing',weapon,'and do',weapons[weapon],'damage..')
		print('\t\t\t\tThe monster now has',mons[1],'health..\n')
	else:
		print('\t\t\t\t',mons[0],'has',mons[1],'health..')
		print('\t\t\t\tYou swing',weapon,'and miss.\n')
	if mons[1] <= 0:
		print('\t\t\t\tYou have defeated',mons[0],', congratulations hero!\n')
		item = choice(nounL)
		adje = choice(adjL)
		print('\t\t\t\tThe enemy leaves behind',item,'that looks',adje,'...')
		mons = None
	else:
		if randrange(10) < 5:
			health -= monsters[mons[0]]-armors[armor]
			print('\t\t\t\tThe monster attacks you for',monsters[mons[0]]-armors[armor],'damage.')
			print('\t\t\t\tYou have',health,' health remaining.\n')
		else:
			print('\t\t\t\tThe monster swings at you but misses.\n')
	if health <= 0:
		print('\t\t\t\tYou have been killed by',mons[0],'... The Emporer\'s reign continues!')
		exit()

def showCommands():
	print('\t\tenter the next room - Makes a new room')
	print('\t\tgrab item - Picks up item in room')
	print('\t\tshow inventory - Shows all items in player inventory')
	print('\t\tequip item - Prompts you to equip an item from inventory')
	print('\t\tshow equipped items - Lists items currently equipped')
	print('\t\tuse potion - Uses a potion if owned, restores 30 health')
	print('\t\tshow current health - shows current player health')
	print('\t\tfight - fights the enemy in the room')
	print('\t\tshow current room - describes the current room')
	print('\t\texit - ends the game')
	print('\t\t')

def begin():
	global item, inventory, weapon, armor, health
	while True:
		command = input('\nWhat would you like to do?\n\t')
		if ('room' in command and\
			('search' not in command and 'describe' not in command\
			and 'show' not in command)):
			if mons is None:
				generateRoom()
			else:
				print('\t\tYou must first defeat the monster.')
		elif ('grab' in command and 'item' in command) or (item is not None and item in command):
			if item is not None:
				if item in collect:
					print('\t\tYou add the item to your inventory.')
					inventory.append(item)
					item = None
				else:
					print('\t\tYou cannot pick up this item.')
			else:
				print('\t\tThere is no item to pick up.')
		elif command == 'exit':
			exit()
		elif 'inventory' in command:
			print('\t\t',inventory)
		elif 'equip' in command:
			print('\t\tThis is your current inventory :\n\t\t\t',inventory,'\n')
			which = input('\t\tWhich item would you like to equip?\n\t\t\t')
			if which in inventory:
				if which in weapons:
					weapon = which
					print('\t\t\t\tYou equip this as your weapon.')
				elif which in armors:
					armor = which
					print('\t\t\t\tYou equip this as your armor.')
				elif which in items:
					print('\t\t\t\tThis item is not equippable.')
			else:
				print('\t\t\t\tYou do not have such an item.')
		elif command == 'show equipped items':
			print('\t\tWeapon :',weapon,'... ( dmg',weapons[weapon],')')
			print('\t\tArmor  :',armor,'... ( def',armors[armor],')')
		elif 'room' in command:
			showRoom()
		elif 'fight' in command or 'attack' in command:
			if mons is not None:
				fight()
			else:
				print('\t\tThere is no monster to fight in this room')
		elif 'potion' in command:
			if 'a potion' in inventory:
				inventory.remove('a potion')
				health += 30
				if health > 100:
					health = 100
				print('\t\tYou use a potion and now have',health,'health.')
			else:
				print('\t\tYou do not have any potions to use.')
		elif 'self' in command or 'health' in command or 'character' in command:
			print('\t\tYou have',health,'health remaining')
		elif 'help' in command or 'commands' in command:
			showCommands()
		else:
			print('\t\tI am not sure what you want me to do. try \'help\'..')

begin()