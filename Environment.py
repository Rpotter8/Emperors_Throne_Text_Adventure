class Environment():
    def __init__(self,entities,desc):
        self.entities = entities
        self.description = desc
    def toString(self):
        retDesc = "You have entered "+self.description+" that contains "
        for i in self.entities:
            retDesc = retDesc+"\n a(n)"+i.toString()
        return retDesc
