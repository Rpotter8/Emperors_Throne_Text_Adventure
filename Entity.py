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
        self.name.replace('',' ')
        self.type = etype
        if etype=="Enemy":
            self.attr1 = attr1 #Health
            self.attr2 = attr2 #Damage
        elif etype=="Key":
            self.attr1 = attr1 #DoorNumber
        elif etype=="Potion":
            self.attr1 = attr1 #Effect
            self.attr2 = attr2 #Severity
        elif etype=="item":
            self.attr1=attr1 #Strength
            self.attr2=attr2 #Defense
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAttr1(self):
        return self.attr1
    def getAttr2(self):
        return self.attr2
    def setAttr2(self,val):
        self.attr2 = val
    def setAttr1(self,val):
        self.attr1 = val
    def toString(self):
        if(self.type == "Enemy"):
            return self.name+" has "+str(self.attr1)+" hitpoints and does "+str(self.attr2)+" damage!"
        elif(self.type=="Key"):
            return self.name+" opens door "+str(self.attr1)
        elif(self.type=="Potion"):
            return self.name
        elif(self.type=="item"):
            if(self.name in Library.getWeaponsList()):
                return self.name+" which does "+str(self.attr1)+" damage"
            elif(self.name in Library.getArmorsList()):
                return self.name+" which does "+str(self.attr2)+" defense"
            else:
                return self.name
        return self.name
    def toStringItem(self):
        return self.name
