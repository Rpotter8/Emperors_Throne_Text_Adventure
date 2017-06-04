from Entity import Entity
import random
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
    def getAttack(self):
        return self.attack
    def setWeapon(self,item):
        self.weapon = item
        self.attack = self.weapon.getAttr1();
        print(str(item.toStringItem())+" is equipped as weapon")
    def setArmor(self,item):
        self.armor = item
        self.defense = self.armor.getAttr2();
        print(str(item.toStringItem())+" is equipped as armor")
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
    def useItem(self,item):
        #print("Tried to use "+item.getName())
        if(item.getType()=="Potion"):
            if item.getAttr1() == 0:
                self.health += item.getAttr2()
                print("You were healed for "+str(item.getAttr2())+" health")
            else:
                self.health -= item.getAttr2()
                print("You were poisened for "+str(item.getAttr2())+" damage")
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
        print("You are now fighting a(n) "+monster.toStringItem()+".")
        while monster.getAttr1() > 0 and self.health > 0:
            chance = random.randint(1,10)
            if chance < 9:
                print("You swing your "+self.weapon.toStringItem()+" and do\n\t"+\
                    str(self.attack)+" damage to the "+monster.toStringItem()+".")
                monster.setAttr1(monster.getAttr1()-self.attack)
                print("\t\tThe monster now has "+str(monster.getAttr1())+" health.\n")
            else:
                print("You swing your "+self.weapon.toStringItem()+" but you miss.\n")
            if monster.getAttr1() <= 0:
                print("You have defeated the"+monster.toStringItem()+"..\n\t"+\
                    "Congratulations, Hero!")
                env.remove(monster)
            else:
                chance = random.randint(1,10)
                if chance < 8:
                    print("The "+monster.toStringItem()+" attacks you and does "+\
                        "\n\t"+str(monster.getAttr2())+" damage.")
                    if self.defense < monster.getAttr2():
                        print("\tYour armor has blocked "+str(self.defense)+" damage.")
                        self.health -= (monster.getAttr2()) - self.defense
                    else:
                        print("\tYour armor blocks all of this enemies damage.")
                    if self.health > 0:
                        print("\tYou have "+str(self.health)+" health remaining, Hero!\n")
                    else:
                        print("\n\n\tThe "+monster.toStringItem()+" has slain you!")
                        print("\tYou have died.")
                        print("\tThe emporers reign continues...")
                        exit()
                else:
                    print("The "+monster.toStringItem()+" swings at you but misses.\n")