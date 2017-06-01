import itertools
#Contains all object names that can be used
Creatures = ["Giant","Dragon","Wolf","Mime","Rat"]

Descriptions = ["Giant","Small","Tiny","Red","Black","Blue","Green","Purple","Translucent"]

collect=['a sword','a helmet','a pair of pants','a shirt',
		'some armor','a blade','a knife','a hammer']

items=['Potion','Gem']

weapons={'a sword':13,'a blade':9,'a knife':6,'a hammer':10,'a stick':2,'dev sword':50}

armors={'a helmet':5,'a pair of pants':3,'a shirt':8,'some armor':13,'rags':1,'dev armor':50}

def getCreatureList():
    return Creatures
def getDescriptionsList():
    return Descriptions
def getCollectList():
    return collect
def getItemsList():
    return items
def getWeaponsList():
    return weapons
def getArmorsList():
    return armors
def getMasterItemList():
    return list(itertools.product(Descriptions,items))
def getEquipsList():
    return getArmorList().keys()+getWeaponsList().keys()
