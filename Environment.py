import Library
#A class designed to model any of the game's environments.
#Contains a description to be given to the user.
#Contains a list of entities that this environment contains.
class Environment():
    def __init__(self,entities,desc,doors,end):
        self.entities = entities
        self.doors = doors
        self.description = desc
        self.end = end
    def changeDesc(self,ndesc):
        self.description = ndesc
    def addItem(self,item):
        self.entities.append(item)
    def toString(self):
        if(len(self.entities)==0):
            retDesc = "\nYou have entered "+self.description+" that is empty. "
        else:
            retDesc = "\nYou have entered "+self.description+" that contains: "
            for i in self.entities:
                #print ("\t\t\t\tDEBUG : ",i)
                if i not in Library.getCollectList():
                    retDesc = retDesc+"\n\t\t a(n) "+i.toString()
                else:
                    retDesc = retDesc+"\n\t\t "+i
        retDesc = retDesc+"\n\tThe exits from this room are:"
        for z in self.doors:
            retDesc = retDesc+"\n\t\t"+z.toString()
        return retDesc
    def hasDoor(self,direction):
        for z in self.doors:
            if(direction == z.getDoorDir() and not z.isLocked()):
                return True
        return False
    def getDoors(self):
        return self.doors
    def unlockDoors(self, key):
        for door in self.doors:
            door.unlock(key)
    def hasItem(self):
        return len(self.entities)>0
    def hasEnemy(self):
        if len(self.getMonsters()) > 0:
        #    print (self.getMonstersSimple())
           return True
        return False
    def lockDoor(self,direction,key):
        for door in self.doors:
            if door.getDoorDir()==direction:
                if door.lock(key):
                    return True
        return False
    def remove(self, item):
        self.entities.remove(item)
    def getMonstersSimple(self):
        return [monster.toStringItem().lower() for monster in self.entities\
                if(monster.toStringItem() in Library.getCreatureList())]
    def getMonsters(self):
        return [monster for monster in self.entities\
                if(monster.toStringItem() in Library.getCreatureList())]
    def getMonstersMap(self):
        monsterDict = {}
        for monster in self.entities:
            if monster.toStringItem() in Library.getCreatureList():
                monsterDict[monster.toStringItem().lower()] = monster
        return monsterDict
    def getItems(self):
        return [item for item in self.entities]
    def containsStairs(self):
        for item in self.entities:
            if item.getType() == "stairs":
                return True
        return False
    def remove(self,obj):
        self.entities.remove(obj)
