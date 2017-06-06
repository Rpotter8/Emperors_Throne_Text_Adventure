import itertools
#Contains all object names that can be used
Creatures = ["Giant","Dragon","Wolf","Mime","Rat","Skeleton","Ogre",\
			"Bandit","Vampire","Zombie","Stone-Gollum","Goblin","Orc"]

Descriptions = ["Large",'Bright','Ancient','Quiet','Scorched','Dirty',\
				'Burnt','Hot','Freezing','Friged','Dark',"Giant","Small",\
				"Tiny","Red","Black","Blue","Green","Purple","Translucent"]

items=['Potion','Gem','Key']

weapons={'sword':13,'sword':13,'sword':13,'sword':13,'sword':13,'sword':13,\
		'sword':13,'sword':13,'sword':13,'sword':13,'sword':13,'sword':13,\
		'blade':9,'blade':9,'blade':9,\
		'blade':9,'blade':9,'blade':9,\
		'dagger':5,'dagger':5,'dagger':5,'dagger':5,'dagger':5,'dagger':5,'dagger':5,\
		'dagger':5,'dagger':5,'dagger':5,'dagger':5,'dagger':5,'dagger':5,'dagger':5,\
		'knife':6,'knife':6,'knife':6,'knife':6,\
		'knife':6,'knife':6,'knife':6,'knife':6,\
		'hammer':10,'hammer':10,'hammer':10,'hammer':10,'hammer':10,\
		'hammer':10,'hammer':10,'hammer':10,'hammer':10,'hammer':10,\
		'stick':2,'stick':2,'stick':2,'stick':2,\
		'stick':2,'stick':2,'stick':2,'stick':2,\
		'greatsword':20,'greatsword':20,'greatsword':20,\
		'greatsword':20,'greatsword':20,'greatsword':20,\
		'greataxe':18,'greataxe':18,\
		'greataxe':18,'greataxe':18,\
		'spear':14,'spear':14,'spear':14,'spear':14,\
		'spear':14,'spear':14,'spear':14,'spear':14,\
		'whip':3,'whip':3,\
		'whip':3,'whip':3,\
		'devsword':50}

armors={'helmet':5,'helmet':5,'helmet':5,'helmet':5,'helmet':5,'helmet':5,\
		'helmet':5,'helmet':5,'helmet':5,'helmet':5,'helmet':5,'helmet':5,\
		'pants':3,'pants':3,'pants':3,'pants':3,'pants':3,\
		'pants':3,'pants':3,'pants':3,'pants':3,'pants':3,\
		'shirt':8,'shirt':8,'shirt':8,'shirt':8,'shirt':8,'shirt':8,'shirt':8,\
		'shirt':8,'shirt':8,'shirt':8,'shirt':8,'shirt':8,'shirt':8,'shirt':8,\
		'armor':15,'armor':15,'armor':15,'armor':15,\
		'armor':15,'armor':15,'armor':15,'armor':15,\
		'rags':1,'rags':1,\
		'rags':1,'rags':1,\
		'chainmail':11,'chainmail':11,'chainmail':11,\
		'chainmail':11,'chainmail':11,'chainmail':11,\
		'skullcap':7,'skullcap':7,\
		'skullcap':7,'skullcap':7,\
		'gauntlets':4,'gauntlets':4,'gauntlets':4,'gauntlets':4,'gauntlets':4,\
		'gauntlets':4,'gauntlets':4,'gauntlets':4,'gauntlets':4,'gauntlets':4,\
		'tiara':2,'tiara':2,\
		'ring':16,'ring':16,'ring':16,\
		'amulet':12,'amulet':12,'amulet':12,\
		'devarmor':50}

def getCreatureList():
	#print([cre.lower() for cre in Creatures])
    return Creatures
def getDescriptionsList():
    return Descriptions
def getCollectList():
    return list(getArmorsList().keys())+list(getWeaponsList().keys())
def getItemsList():
    return items
def getWeaponsList():
    return weapons
def getArmorsList():
    return armors
def getMasterItemList():
    itemList = list(itertools.product(Descriptions,items))
    returnlist = []
    for item in itemList:
        returnlist.append(''.join(item))
    return returnlist
def getEquipsList():
    return list(getArmorsList().keys())+list(getWeaponsList().keys())
