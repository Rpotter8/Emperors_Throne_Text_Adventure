from Entity import Entity
import random
import time
import sys
import simpleaudio as sa
import os

wave_obj = sa.WaveObject.from_wave_file("attack.wav")

def dprint(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.025)
    time.sleep(.3)
    print()

def sound():
    os.system("tput bel")
    play = wave_obj.play()
    play.wait_done()

class Player():
    def __init__(self,name,health,attack):
        self.pos = [0,0]
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = 2
        self.inventory = [Entity("a stick","item",2,2),\
                            Entity("rags","item",2,2)]
        self.weapon = Entity("a stick","item",2,2)
        self.armor = Entity("rags","item",2,2)
    def damage(self,amount):
        self.health = self.health-amount
        if self.health<=0:
            return "Dead"
    def heal(self,amount):
        self.health = self.health+amount
    def getHealth(self):
        return self.health
    def getDefense(self):
        return self.defense
    def getAttack(self):
        return self.attack
    def getName(self):
        return self.name
    def setWeapon(self,item):
        self.weapon = item
        self.attack = self.weapon.getAttr1();
        dprint(str(item.toStringItem())+" is equipped as weapon")
    def setArmor(self,item):
        self.armor = item
        self.defense = self.armor.getAttr2();
        dprint(str(item.toStringItem())+" is equipped as armor")
    def getWeapon(self):
        return self.weapon
    def getArmor(self):
        return self.armor
    def changeAttack(self,number):
        self.attack = number
    def getInventory(self):
        lis = []
        for item in self.inventory:
            lis.append(item.toStringItem())
        return lis
    def getInventoryComplex(self):
        return self.inventory
    def addInventory(self,obj):
        self.inventory.append(obj)
    def removeInventory(self,index):
        inventory.pop(index)
    def getName(self):
        return self.name
    def setLocation(self,x,y):
        self.pos[0] = y
        self.pos[1] = x
    def useItem(self,item):
        #print("Tried to use "+item.getName())
        if(item.getType()=="Potion"):
            if item.getAttr1() == 0:
                self.health += item.getAttr2()
                dprint(str("You were healed for "+str(item.getAttr2())+" health"))
            else:
                self.health -= item.getAttr2()
                dprint(str("You were poisoned for "+str(item.getAttr2())+" damage"))
        self.inventory.remove(item)
    def move(self,direction):
        if(direction == "Up"):
            self.pos[1] = self.pos[1]-1
        if(direction == "Down"):
            self.pos[1] = self.pos[1]+1
        if(direction == "Left"):
            self.pos[0] = self.pos[0]-1
        if(direction == "Right"):
            self.pos[0] = self.pos[0]+1
    def getLocation(self):
        return self.pos
    def fight(self, monster,env):
        dprint(str("You are now fighting a(n) "+monster.toStringItem()+"."))
        while monster.getAttr1() > 0 and self.health > 0:
            chance = random.randint(1,10)
            if chance < 9:
                dprint(str("You swing your "+self.weapon.toStringItem()+" and do\n\t"+\
                    str(self.attack)+" damage to the "+monster.toStringItem()+"."))
                sound()
                monster.setAttr1(monster.getAttr1()-self.attack)
                dprint(str("\t\tThe monster now has "+str(monster.getAttr1())+" health.\n"))
            else:
                dprint(str("You swing your "+self.weapon.toStringItem()+" but you miss.\n"))
            if monster.getAttr1() <= 0:
                dprint(str("You have defeated the "+monster.toStringItem()+"..\n\t"+\
                    "Congratulations, Hero!"))
                dprint(str("You have "+str(self.health)+"health remaining.\n"))
                env.remove(monster)
            else:
                chance = random.randint(1,10)
                if chance < 8:
                    dprint(str("The "+monster.toStringItem()+" attacks you and does "+\
                        "\n\t"+str(monster.getAttr2())+" damage."))
                    sound()
                    if self.defense < monster.getAttr2():
                        dprint(str("\tYour armor has blocked "+str(self.defense)+" damage."))
                        self.health -= (monster.getAttr2()) - self.defense
                    else:
                        dprint("\tYour armor blocks all of this enemies damage.")
                    if self.health > 0:
                        dprint(str("\tYou have "+str(self.health)+" health remaining, Hero!\n"))
                    else:
                        dprint(str("\n\n\tThe "+monster.toStringItem()+" has slain you!"))
                        dprint("\tYou have died.")
                        dprint("\tThe emporers reign continues...")
                        exit()
                else:
                    dprint(str("The "+monster.toStringItem()+" swings at you but misses.\n"))
