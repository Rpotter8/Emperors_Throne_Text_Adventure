import Library
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
        elif etype=="item":
            self.strength=attr1
            self.defense=attr2
            
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAttr1(self):
        if self.type=="Enemy":
            return self.health
        elif self.type=="Key":
            return self.doornum
        elif self.type=="Potion":
            return self.effect
        elif self.type=="item":
            return self.strength
    def getAttr2(self):
        if self.type=="Enemy":
            return self.damage
        elif self.type=="Key":
            return self.doornum
        elif self.type=="Potion":
            return self.severity
        elif self.type=="item":
            return self.defense
    def setAttr2(self,val):
        if self.type=="Enemy":
            self.damage = val
        elif self.type=="Key":
            self.doornum = val
        elif self.type=="Potion":
            self.severity = val
        elif self.type=="item":
            self.defense = val
    def setAttr1(self,val):
        if self.type=="Enemy":
            self.health = val
        elif self.type=="Key":
            self.doornum = val
        elif self.type=="Potion":
            self.effect = val
        elif self.type=="item":
            self.strength = val
    def toString(self):
        if(self.type == "Enemy"):
            return self.name+" has "+str(self.health)+" hitpoints and does "+str(self.damage)+" damage!"
        elif(self.type=="Key"):
            return self.name+" opens door "+str(self.doornum)
        elif(self.type=="Potion"):
            return self.name
        elif(self.type=="item"):
            if(self.name in Library.getWeaponsList()):
                return self.name+" which does "+str(self.strength)+" damage"
            elif(self.name in Library.getArmorsList()):
                return self.name+" which does "+str(self.defense)+" defense"
            else:
                return self.name
        else:
            return "SOMETHING WENT WRONG WITH ITEM"
    def toStringItem(self):
        if(self.type=='item' or self.type=='Enemy'):
            return self.name
        else:
            return "SOMETHING WENT WRONG WITH ITEM"
