from Player import *
from Environment import *
import Library
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
                print("You have added ",item.toString()," to your inventory.")
        return "Grab"
    if("inventory" in data):
        inv = plyr.getInventory()
        print (inv)
        return "Inventory"
    if("equipment" in data):
        armor = plyr.getArmor()
        weapon = plyr.getWeapon()
        print ("This is your weapon : ",weapon.toString())
        print ("This is your armor  : ",armor.toString())
        return "Equipment"
    if("equip" in data):
        comp = plyr.getInventoryComplex()
        inv = plyr.getInventory()
        print (inv)
        equip=input("\tThis is your Inventory, which would you like to equip?\n\t\t")
        if equip in inv:
            print ("you have this item!!!");
            if equip in Library.getWeaponsList():
                for item in comp:
                    if item.toStringItem() == equip:
                        plyr.setWeapon(item)
            elif equip in Library.getArmorsList():
                for item in comp:
                    if item.toStringItem() == equip:
                        plyr.setArmor(item)
        else :
            print ("YOU DONT HAVE THIS@!!!@##R")
        return "Equip"
    if("fight" in data or "attack" in data):
        monLis = env.getMonsters()
        monsters = env.getMonstersSimple()
        print (monsters)
        monster = input("\tWhich would you like to fight?\n\t\t")
        if monster in monsters:
            print ("this monster is in room!")
        else:
            print ("This monster isnt real@@@@@#")
    return "Error"+data
