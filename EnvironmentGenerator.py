#Generates Valid New Environments
from Entity import * 
import random
from Environment import *
import Library

def genObject(objType, difficulty):
    NUMBER_OF_DOORS = 10
    retEnt = ""
    if objType == 0:
        #BuildRandomEnemy Object Here
        Creatures = Library.getCreatureList()
        Choice = random.randint(0,len(Creatures)-1)
        retEnt = Entity(Creatures[Choice],"Enemy",difficulty*random.randint(1,3),difficulty*random.randint(1,3))
    elif objType == 1:
        #BuildRandomKey Object Here
        Descriptions = Library.getDescriptionsList()
        Choice = random.randint(0,len(Descriptions)-1)
        retEnt = Entity(Descriptions[Choice]+" Key","Key",random.randint(0,NUMBER_OF_DOORS-1),0)
    elif objType == 2:
        #BuildRandomPotion Object Here
        Descriptions = Library.getDescriptionsList()
        Choice = random.randint(0,len(Descriptions)-1)
        retEnt = Entity(Descriptions[Choice]+" Potion","Potion",0,5)
    return retEnt;

def genEnvironment(difficulty):
    objects = []
    numObjects = random.randint(0,2)
    for i in range(0,numObjects):
        objType = random.randint(0,2)
        objects.append(genObject(objType,difficulty))
    #Generate random room description
    desc = "a small room"
    retEnv = Environment(objects,desc)
    return retEnv
        

