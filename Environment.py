import Library
#A class designed to model any of the game's environments.
#Contains a description to be given to the user.
#Contains a list of entities that this environment contains.
class Environment():
    def __init__(self,entities,desc,doors):
        self.entities = entities

        self.doors = doors
        self.description = desc
    def changeDesc(self,ndesc):
        self.description = ndesc
    def addItem(self,item):
        self.entities.append(item)
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
    def getItems(self):
        #for z in self.entities:
        #    print("\t\tDEBUG : ",str(type(z)))
        #    print("\t\t\tDEBUG : ",str(z.toString()))
        lis = []
        #print (self.entities)
        #print (Library.getCollectList())
        for item in self.entities:
            if(item.getType != "Enemy"):
                lis.append(item)
        #print (lis)
        #print ([item for item in self.entities if(item.toStringItem() in Library.getCollectList())])
        #return [item for item in self.entities if(item.toStringItem() in Library.getCollectList())]
        return lis
