from Player import *
from Environment import *
import Library
import nltk

import json





def processInput(data,plyr,env):
    data = "I " + data.lower()

    words = nltk.word_tokenize(data)
    words = nltk.pos_tag(words)
    print(words)

    with open('corpus/thes.nofinal', 'r') as myfile:
        thes=myfile.read().replace('\n', '')

    verb = ""
    action = ""
    for i in words:
        if(i[1] == "VBP" or i[1] == "VBD" or i[1] == "VBZ"):
            verb = i[0]
        if(i[1] == "RB" or i[1] == "RP" or i[1] == "NNS" or
            i[1] == "NN" or i[1] == "JJ"):
            action = i[0]
        if(verb != "" and action != ""):
            print("Verb: " + verb +", Action: " + action)
            break


    thes = json.loads(thes)



    if("up" == action or "up" == verb or "north" == action):
        if(env.hasDoor("Up")):
            plyr.move("Up")
            return "Up"
        else:
            return "Errorrun into wall"
    if("down" == action or "down" == verb or "south" == action):
        if(env.hasDoor("Down")):
            plyr.move("Down")
            return "Down"
        else:
            return "Errorrun into wall"
    if("left" == action or "left" == verb or "west" == action):
        if(env.hasDoor("Left")):
            plyr.move("Left")
            return "Left"
        else:
            return "Errorrun into wall"
    if("right" == action or "right" == verb or "east" == action):
        if(env.hasDoor("Right")):
            plyr.move("Right")
            return "Right"
        else:
            return "Errorrun into wall"
    if("look" == verb):
        return "Look"
    if("grab" == verb or verb in thes["data"]["grab"]["t1"]):
        #print(data)
        if(env.hasItem()):
            for item in env.getItems():
                #print(tuple(item.getName().split(" ")))
                if (((item.getName().lower() in Library.getEquipsList()) or (item.getName().lower() in Library.getMasterItemList())) and (item.getName().lower() == action)):
                    plyr.addInventory(item)
                    env.remove(item)
                    print("You have added ",item.toString()," to your inventory.")
        return "Grab"
    if("inventory" == action or action in thes["data"]["inventory"]["t1"]):
        inv = plyr.getInventory()
        print (inv)
        return "Inventory"
    if("equipment" == action or action in thes["data"]["equipment"]["t1"]):
        armor = plyr.getArmor()
        weapon = plyr.getWeapon()
        print ("This is your weapon : ",weapon.toString())
        print ("This is your armor  : ",armor.toString())
        return "Equipment"
    if("equip" == verb or verb in thes["data"]["equip"]["t1"]):
        comp = plyr.getInventoryComplex()
        inv = plyr.getInventory()
        #print (inv)
        #equip=input("\tThis is your Inventory, which would you like to equip?\n\t\t")
        if action.lower() in [x.lower() for x in inv]:
            #print ("you have this item!!!");
            if action.lower() in Library.getWeaponsList():
                for item in comp:
                    if item.toStringItem() == action.lower():
                        plyr.setWeapon(item)
            elif action.lower() in Library.getArmorsList():
                for item in comp:
                    if item.toStringItem() == action.lower():
                        plyr.setArmor(item)
        else :
            print ("YOU DONT HAVE THIS!")
        return "Equip"
    #if("key" == verb):
    #    comp = plyr.getInventoryComplex()
    #    inv = plyr.getInventory()
    #    #Hardcoded key zero check
    #    for item in comp:
            #print(item.getName())
            #print(item.getAttr1())
    #        if item.getType() == "Key":
                #print("Using Key")
                #print(env.getDoors())
    #            env.unlockDoors(item.getAttr1())
    #    return "Key"

    if("use" == verb or verb in thes["data"]["use"]["t1"]):
        comp = plyr.getInventoryComplex()
        inv = plyr.getInventory()
        #print(inv)
        #use=input("\tThis is your Inventory, what would you like to use?\n\t\t")
        if action.lower() in [x.lower() for x in inv]:
            #print("You have this item!!!")
            #print(Library.getMasterItemList())
            #print(use.split(" "))
            if action.lower() in Library.getMasterItemList():
                #print("Found in list")
                for item in comp:
                    if item.getName().lower() == action.lower():
                        #print("Found Specific Item")
                        #print(item.getType())
                        if item.getType() == "Key":
                            #print("Using Key")
                            #print(env.getDoors())
                            env.unlockDoors(item.getAttr1())
                            return "Unlocked"
                        else:
                            plyr.useItem(item)
        else :
            print ("YOU DONT HAVE THIS!")
            return "ErrorUsing item."
        return "Use"
    if("fight" == verb or "attack" == verb or verb in thes["data"]["fight"]["t1"]):
        monLis = env.getMonstersMap()
        #monster = input("\tWhich would you like to fight?\n\t\t")
        if action.lower() in monLis.keys():
            print ("\nBrace yourself, Hero, for a battle commences!\n")
            plyr.fight(monLis[action.lower()],env)
        else:
            print ("\tThis monster isn't in the room with you.\n")
        return "Fight"
    if("stairs" == action):
        if env.containsStairs():
            return "Stairs"
    if(action.lower() == "condition" or action.lower() in thes["data"]["condition"]["t1"]):
        return "Condition"
    return "Error"+verb
