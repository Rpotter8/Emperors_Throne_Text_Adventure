#Generates Valid New Environments
from Entity import * 
import random
from Environment import *
from Door import *
import Library

NUMBER_OF_DOORS = 10
def genObject(objType, difficulty):
    retEnt = ""
    if objType == 0:
        #BuildRandomEnemy Object Here
        Creatures = Library.getCreatureList()
        Choice = random.choice(Creatures)
        retEnt = Entity(Choice,"Enemy",difficulty*random.randint(1,3),\
                difficulty*random.randint(1,3))
    elif objType == 1:
        #BuildRandomKey Object Here
        Descriptions = Library.getDescriptionsList()
        Choice = random.randint(0,len(Descriptions)-1)
        retEnt = Entity(Descriptions[Choice]+" Key","Key",\
                random.randint(0,NUMBER_OF_DOORS-1),0)
    elif objType == 2:
        #BuildRandomPotion Object Here
        Descriptions = Library.getDescriptionsList()
        Choice = random.randint(0,len(Descriptions)-1)
        #TODO Randomize Potion Effect
        retEnt = Entity(Descriptions[Choice]+" Potion","Potion",0,5)
    elif objType >= 3:
        #BuildRandomItem object here:
        print("DEBUG : WE MADE IT BOIZ")
        items = Library.getCollectList()
        Choice = random.choice(items)
        retEnt = Entity(Choice,"item",random.randint(7,14)-difficulty,\
            random.randint(7,14)-difficulty)
    return retEnt;

def genEnvironment(difficulty,updoor,downdoor,rightdoor,leftdoor):
    objects = []
    door = []
    choices = []
    if updoor == 1:
        door.append(Door(False,"Up",0))
    if downdoor == 1:
        door.append(Door(False,"Down",0))
    if rightdoor == 1:
        door.append(Door(False,"Right",0))
    if leftdoor == 1:
        door.append(Door(False,"Left",0))
    numObjects = random.randint(0,2)
    for i in range(0,numObjects):
        objType = random.randint(0,6)
        objects.append(genObject(objType,difficulty))
    #Generate random room description
    #TODO make the description more random
    Descriptions = Library.getDescriptionsList()
    Choice = random.randint(0,len(Descriptions)-1)
    desc = "a "+Descriptions[Choice]+" room"
    retEnv = Environment(objects,desc,door)
    return retEnv
        

