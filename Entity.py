#Class which contains information for objects in the game
#Attributes are assigned based on object type
    #Enemies have attributes health and damage
    #Keys have attribute doornum (the id of the door they open)
    #Potions have attributes effect and severity
        #Potion Effects are: 0 = health, 1 = poison
class Entity():
    def __init__(self,name,etype,attr1,attr2):
        self.name = name
        self.type = etype
        if etype=="Enemy":
            self.health = attr1
            self.damage = attr2
        elif etype=="Key":
            self.doornum = attr1
        elif etype=="Potion":
            self.effect = attr1
            self.severity = attr2
            
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAttr1(self):
        return self.attr1
    def getAttr2(self):
        return self.attr2
    def toString(self):
        if(self.type == "Enemy"):
            return self.name+" has "+str(self.health)+" hitpoints and does "+str(self.damage)+" damage!"
        elif(self.type=="Key"):
            return self.name+" opens door "+str(self.doornum)
        elif(self.type=="Potion"):
            return self.name+" heals "+str(self.severity)+" hitpoints!"
