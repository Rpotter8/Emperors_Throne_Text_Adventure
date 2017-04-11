class Player():
    def __init__(self,name,health,attack):
        self.pos = [0,0]
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = []
    def damage(self,amount):
        self.health = self.health-amount
        if self.health<=0:
            return "Dead"
    def heal(self,amount):
        self.health = self.health+amount
    def getAttack(self):
        return self.attack
    def changeAttack(self,number):
        self.attack = number
    def getInventory(self):
        return self.inventory
    def addInventory(self,obj):
        self.inventory.append(obj)
    def removeInventory(self,index):
        inventory.pop(index)
    def getName(self):
        return self.name
    def move(self,direction):
        if(direction == "Up"):
            self.pos[1] = self.pos[1]+1
        if(direction == "Down"):
            self.pos[1] = self.pos[1]-1
        if(direction == "Left"):
            self.pos[0] = self.pos[0]-1
        if(direction == "Right"):
            self.pos[0] = self.pos[0]+1
