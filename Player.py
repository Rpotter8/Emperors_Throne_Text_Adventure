from Entity import Entity
class Player():
    def __init__(self,name,health,attack):
        self.pos = [0,0]
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = [Entity("a stick","item",2,2),Entity("rags","item",2,2)]
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
        print(str(item.toStringItem())+" is equipped as weapon")
    def setArmor(self,item):
        self.armor = item
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
