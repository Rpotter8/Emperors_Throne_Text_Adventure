from Player import *
from Environment import *
def processInput(data,plyr,env):
    data = data.lower()
    if("up" in data):
        if(env.hasDoor("Up")):
            plyr.move("Up")
            return "Up"
        else:
            return "Errorrun into wall"
    if("down" in data):
        if(env.hasDoor("Down")):
            plyr.move("Down")
            return "Down"
        else:
            return "Errorrun into wall"
    if("left" in data):
        if(env.hasDoor("Left")):
            plyr.move("Left")
            return "Left"
        else:
            return "Errorrun into wall"
    if("right" in data):
        if(env.hasDoor("Right")):
            plyr.move("Right")
            return "Right"
        else:
            return "Errorrun into wall"
    if("look" in data):
        return "Look"
    if("grab" in data):
        if(env.hasItem()):
            for item in env.getItems():
                plyr.addInventory(item)
                env.remove(item)
                print("You have added ",item," to your inventory.")
        return "Grab"
    return "Error"+data
