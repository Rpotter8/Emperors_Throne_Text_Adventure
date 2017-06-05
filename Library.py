import itertools
#Contains all object names that can be used
Creatures = ["Giant","Dragon","Wolf","Mime","Rat"]

Descriptions = ["Giant","Small","Tiny","Red","Black","Blue","Green","Purple","Translucent"]

items=['Potion','Gem','Key']

weapons={'sword':13,'blade':9,'knife':6,'hammer':10,'stick':2,'devsword':50}

armors={'helmet':5,'pair of pants':3,'shirt':8,'armor':13,'rags':1,'devarmor':50}

def getCreatureList():
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
