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
        retEnt = Entity(Choice,"Enemy",difficulty*random.randint(10,15)+difficulty-random.randint(0,3),\
                difficulty*random.randint(8,14)+(difficulty*2)-random.randint(0,3))
    elif objType == 1:
        #BuildRandomKey Object Here
        Descriptions = Library.getDescriptionsList()
        Choice = random.randint(0,len(Descriptions)-1)
        #Removed Random Keydrop, always door 0
        retEnt = Entity(Descriptions[Choice]+"Key","Key",0,0)
                #random.randint(0,NUMBER_OF_DOORS-1),0)
    elif objType == 2:
        #BuildRandomPotion Object Here
        Descriptions = Library.getDescriptionsList()
        Choice = random.randint(0,len(Descriptions)-1)
        #TODO Randomize Potion Effect CURRENTLY ALWAYS HEAL 5 POINTS
        retEnt = Entity(Descriptions[Choice]+"Potion","Potion",0,5)
    elif objType >= 3:
        #BuildRandomItem object here:
        items = Library.getCollectList()
        Choice = random.choice(items)
        armors = Library.getArmorsList()
        weapons = Library.getArmorsList()
        if Choice in armors:
            base = armors[Choice]
        elif Choice in weapons:
            base = weapons[Choice]
        else:
            base =0
        retEnt = Entity(Choice,"item",random.randint(4,10)-difficulty+base,\
            random.randint(4,10)-difficulty+base)
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
        objType = random.randint(0,3)
        #Removed Random Key Generation, only one key per floor now.
        while objType == 1:
            objType = random.randint(0,3)
        objects.append(genObject(objType,difficulty))
    #Generate random room description
    #TODO make the description more random
    Descriptions = Library.getDescriptionsList()
    Choice = random.randint(0,len(Descriptions)-1)
    desc = "a "+Descriptions[Choice]+" room"
    retEnv = Environment(objects,desc,door,False)
    return retEnv
