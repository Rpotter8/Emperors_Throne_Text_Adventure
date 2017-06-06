from Player import *
from Environment import *
import Library
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
    data = data.lower()
    if("up" in data):
        if(env.hasEnemy()):
            dprint("The monster blocks you path.\n")
            return "Fail"
        if(env.hasDoor("Up")):
            plyr.move("Up")
            return "Up"
        else:
            return "Errorrun into wall"
    if("down" in data):
        if(env.hasEnemy()):
            dprint("The monster blocks you path.\n")
            return "Fail"
        if(env.hasDoor("Down")):
            plyr.move("Down")
            return "Down"
        else:
            return "Errorrun into wall"
    if("left" in data):
        if(env.hasEnemy()):
            dprint("The monster blocks you path.\n")
            return "Fail"
        if(env.hasDoor("Left")):
            plyr.move("Left")
            return "Left"
        else:
            return "Errorrun into wall"
    if("right" in data):
        if(env.hasEnemy()):
            dprint("The monster blocks you path.\n")
            return "Fail"
        if(env.hasDoor("Right")):
            plyr.move("Right")
            return "Right"
        else:
            return "Errorrun into wall"
    if("look" in data):
        return "Look"
    if("grab" in data):
        #print(data)
        if(env.hasItem()):
            for item in env.getItems():
                #print(tuple(item.getName().split(" ")))
                if (((item.getName() in Library.getEquipsList()) or (item.getName() in Library.getMasterItemList())) and (item.getName().lower() in data)):
                    plyr.addInventory(item)
                    env.remove(item)
                    dprint(str("You have added ",item.toString()," to your inventory."))
        return "Grab"
    if("inventory" in data):
        inv = plyr.getInventory()
        dprint (str(inv))
        return "Inventory"
    if("equipment" in data):
        armor = plyr.getArmor()
        weapon = plyr.getWeapon()
        dprint (str("This is your weapon : ",weapon.toString()))
        dprint (str("This is your armor  : ",armor.toString()))
        return "Equipment"
    if("equip" in data):
        comp = plyr.getInventoryComplex()
        inv = plyr.getInventory()
        dprint (inv)
        equip=input("\tThis is your Inventory, which would you like to equip?\n\t\t")
        if equip in inv:
            print ("\n");
            if equip in Library.getWeaponsList():
                for item in comp:
                    if item.toStringItem() == equip:
                        plyr.setWeapon(item)
            elif equip in Library.getArmorsList():
                for item in comp:
                    if item.toStringItem() == equip:
                        plyr.setArmor(item)
        else :
            print ("\n")
        return "Equip"
    if("key" in data):
        comp = plyr.getInventoryComplex()
        inv = plyr.getInventory()
        #Hardcoded key zero check
        for item in comp:
            #print(item.getName())
            #print(item.getAttr1())
            if item.getType() == "Key":
                #print("Using Key")
                #print(env.getDoors())
                env.unlockDoors(item.getAttr1())
        return "Key"
                    
    if("use" in data):
        comp = plyr.getInventoryComplex()
        inv = plyr.getInventory()
        print(inv)
        dprint("\tThis is your Inventory, what would you like to use?\n\t\t")
        use=input()
        if use in inv:
            print("\n")
            #print(Library.getMasterItemList())
            #print(use.split(" "))
            if tuple(use.split(" ")) in Library.getMasterItemList():
                for item in comp:
                    if item.getType() == "Key":
                        #print("Using Key")
                        #print(env.getDoors())
                        env.unlockDoors(item.getAttr1)
                        return "Unlocked"
                    if item.toStringItem() == use:
                        plyr.useItem(item)
        else :
            print ("\n")
            return "ErrorUsing item."
        return "Use"
    if("fight" in data or "attack" in data):
        monLis = env.getMonstersMap()
        if len(env.getMonsters()) == 1:
            dprint (str("\nBrace yourself, "+plyr.getName()+", for a battle commences!\n"))
            for mon in monLis:
                plyr.fight(monLis[mon],env)
            return "Fight"
        dprint("\tYou have multiple adversaries!\nWhich would you like to fight?\n\t\t") 
        monster = input()
        if monster.lower() in monLis.keys():
            dprint (str("\nBrace yourself, "+plyr.getName()+", for a battle commences!\n"))
            plyr.fight(monLis[monster],env)
        else:
            dprint ("\tThis monster isn't in the room with you.\n")
        return "Fight"
    if("stairs" in data):
        if env.containsStairs():
            return "Stairs"
    return "Error"+data
