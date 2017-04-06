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

def genEnvironment(difficulty,direction):
    objects = []
    door = []
    choices = []
    if direction == "Up":
        door.append(Door(False,"Down",0))
        choices = ["Up","Left","Right"]
    elif direction == "Down":
        door.append(Door(False,"Up",0))
        choices = ["Down","Left","Right"]
    elif direction == "Left":
        door.append(Door(False,"Right",0))
        choices = ["Up","Left","Down"]       
    elif direction == "Right":
        door.append(Door(False,"Left",0))
        choices = ["Up","Down","Right"]
    for x in range(0,3):
        randDoorChance = random.randint(0,99)
        isDoor = False
        if randDoorChance < 35:
            isDoor = True
        if isDoor == True:
            randDoor = random.randint(0,len(choices)-1)
            lockedChance = random.randint(0,100/difficulty)
            lockedState = False
            if lockedChance <= 10:
                lockedState = True
            door.append(Door(lockedState,choices[randDoor],random.randint(0,NUMBER_OF_DOORS-1)))
            choices.pop(randDoor)
    numObjects = random.randint(0,2)
    for i in range(0,numObjects):
        objType = random.randint(0,2)
        objects.append(genObject(objType,difficulty))
    #Generate random room description
    Descriptions = Library.getDescriptionsList()
    Choice = random.randint(0,len(Descriptions)-1)
    desc = "a "+Descriptions[Choice]+" room"
    retEnv = Environment(objects,desc,door)
    return retEnv
        

