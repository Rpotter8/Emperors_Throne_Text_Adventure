from Player import *
from Environment import *
import Library
import nltk

import json
import time
import sys

def dprint(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.025)
    time.sleep(.3)
    print()





def processInput(data,plyr,env):
    data = "I " + data.lower()

    words = nltk.word_tokenize(data)
    words = nltk.pos_tag(words)


    with open('corpus/thes.nofinal', 'r') as myfile:
        thes=myfile.read().replace('\n', '')

    verb = ""
    action = ""
    for i in words:
        #print(i[0]+":"+i[1])
        if(i[1] == "VBP" or i[1] == "VBD" or i[1] == "VBZ" or i[1]=="VB"):
            verb = i[0]
        if(i[1] == "RB" or i[1] == "RP" or i[1] == "NNS" or
            i[1] == "NN" or i[1] == "JJ"):
            action = i[0]
        if(verb != "" and action != ""):
            break
    #print(verb+" "+action)

    thes = json.loads(thes)



    if("up" == action or "up" == verb or "north" == action):
        if(env.hasEnemy()):
            return "Fail"
        if(env.hasDoor("Up")):
            plyr.move("Up")
            return "Up"
        else:
            return "Errorrun into wall"
    if("down" == action or "down" == verb or "south" == action):
        if(env.hasEnemy()):
            return "Fail"
        if(env.hasDoor("Down")):
            plyr.move("Down")
            return "Down"
        else:
            return "Errorrun into wall"
    if("left" == action or "left" == verb or "west" == action):
        if(env.hasEnemy()):
            return "Fail"
        if(env.hasDoor("Left")):
            plyr.move("Left")
            return "Left"
        else:
            return "Errorrun into wall"
    if("right" == action or "right" == verb or "east" == action):
        if(env.hasEnemy()):
            return "Fail"
        if(env.hasDoor("Right")):
            plyr.move("Right")
            return "Right"
        else:
            return "Errorrun into wall"    
    if("stairs" == action.lower() or "stairs" == verb.lower()):
        if env.containsStairs():
            return "Stairs"
    if("help" == action.lower() or "help" == verb.lower()):
        return "Help"
    levels = ["t1","t2"]
    for level in levels:
        #print(level)
        if("look" == verb or verb in thes["data"]["look"][level]):
            return "Look"
        if("grab" == verb or verb in thes["data"]["grab"][level]):
        #print(data)
            if(env.hasItem()):
                for item in env.getItems():
                #print(tuple(item.getName().split(" ")))
                    if (((item.getName().lower() in Library.getEquipsList()) or (item.getName().lower() in Library.getMasterItemList())) and (item.getName().lower() == action)):
                        plyr.addInventory(item)
                        env.remove(item)
                        dprint(str("You have added "+item.toString()+" to your inventory."))
            return "Grab"
        if("inventory" == action or action in thes["data"]["inventory"][level]):
            inv = plyr.getInventory()
            dprint (str(inv))
            return "Inventory"
        if("equipment" == action or action in thes["data"]["equipment"][level]):
            armor = plyr.getArmor()
            weapon = plyr.getWeapon()
            dprint (str("This is your weapon : "+weapon.toString()))
            dprint (str("This is your armor  : "+armor.toString()))
            return "Equipment"
        if("equip" == verb or verb in thes["data"]["equip"][level]):
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
                dprint ("YOU DONT HAVE THIS!")
            return "Equip"
        if("use" == verb or verb in thes["data"]["use"][level]):
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
                dprint ("YOU DONT HAVE THIS!")
                return "ErrorUsing item."
            return "Use"
        if("fight" == verb or "attack" == verb or verb in thes["data"]["fight"][level]):
            monLis = env.getMonstersMap()
        #monster = input("\tWhich would you like to fight?\n\t\t")
            if action.lower() in monLis.keys():
                dprint (str("\nBrace yourself, "+plyr.getName()+", for a battle commences!\n"))
                plyr.fight(monLis[action.lower()],env)
            else:
                dprint ("\tThis monster isn't in the room with you.\n")
            return "Fight"
        if(action.lower() == "condition" or action.lower() in thes["data"]["condition"]["t1"]):
            return "Condition"
        
    return "Error"+verb
