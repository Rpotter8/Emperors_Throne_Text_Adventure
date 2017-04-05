#Generates Valid New Environments
from Entity import * 
import random
from Environment import *
import Library

def genObject(objType, difficulty):
    retEnt = ""
    if objType == 0:
        #BuildRandomEnemy Object Here
        Creatures = Library.getCreatureList()
        Choice = random.randint(0,len(Creatures)-1)
        retEnt = Entity(Creatures[Choice],"Enemy",difficulty*random.randint(1,3),difficulty*random.randint(1,3))
    elif objType == 1:
        #BuildRandomKey Object Here
        retEnt = Entity("Dull Key","Key",1,0)
    elif objType == 2:
        #BuildRandomPotion Object Here
        retEnt = Entity("Non-Descript Potion","Potion",0,5)
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
        

