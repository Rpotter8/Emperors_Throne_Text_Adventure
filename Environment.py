#A class designed to model any of the game's environments.
#Contains a description to be given to the user.
#Contains a list of entities that this environment contains.
class Environment():
    def __init__(self,entities,desc):
        self.entities = entities
        self.description = desc
    def toString(self):
        retDesc = "You have entered "+self.description+" that contains "
        for i in self.entities:
            retDesc = retDesc+"\n a(n)"+i.toString()
        return retDesc
