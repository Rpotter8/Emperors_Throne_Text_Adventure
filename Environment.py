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
                retDesc = retDesc+"\n a(n)"+i.toString()
        retDesc = retDesc+"\nThe exits from this room are"
        for z in self.doors:
            retDesc = retDesc+"\n"+z.toString()
        return retDesc
    def hasDoor(self,direction):
        for z in self.doors:
            if(direction in z.getDoorDir()):
                return True
        return False
