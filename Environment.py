import Library
#A class designed to model any of the game's environments.
#Contains a description to be given to the user.
#Contains a list of entities that this environment contains.
class Environment():
    def __init__(self,entities,desc,doors):
        self.entities = entities

        self.doors = doors
        self.description = desc
    def toString(self):
        if(len(self.entities)==0):
            retDesc = "You have entered "+self.description+" that is empty "
        else:
            retDesc = "You have entered "+self.description+" that contains "
            for i in self.entities:
                print ("\t\t\t\tDEBUG : ",i)
                if i not in Library.getCollectList():
                    retDesc = retDesc+"\n a(n)"+i.toString()
                else:
                    retDesc = retDesc+"\n "+i
        retDesc = retDesc+"\nThe exits from this room are"
        for z in self.doors:
            retDesc = retDesc+"\n"+z.toString()
        return retDesc
    def hasDoor(self,direction):
        for z in self.doors:
            if(direction in z.getDoorDir()):
                return True
        return False
    def hasItem(self):
        return len(self.entities)>0
    def remove(self, item):
        self.entities.remove(item)
    def getMonstersSimple(self):
        return [monster.toStringItem() for monster in self.entities\
                if(monster.toStringItem() in Library.getCreatureList())]
    def getMonsters(self):
        return [monster for monster in self.entities\
                if(monster.toStringItem() in Library.getCreatureList())]
    def getMonstersMap(self):
        monsterDict = {}
        for monster in self.entities:
            if monster.toStringItem() in Library.getCreatureList():
                monsterDict[monster.toStringItem()] = monster
        return monsterDict
    def getItems(self):
        return [item for item in self.entities\
                if(item.toStringItem() in Library.getCollectList())]
    def remove(self,obj):
        self.entities.remove(obj)