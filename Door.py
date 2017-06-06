#A class which models all of the game's doors
#Has unlock methods, and methods to get info from the door.
class Door():
    def __init__(self,locked,direction,doorNum):
        self.locked = locked
        self.direction = direction
        self.doorNum = doorNum
    def isLocked(self):
        return self.locked
    def lock(self, key):
        self.doorNum = key;
        self.locked = True;
    def unlock(self,key):
        #print("Attempting to unlock")
        #print(str(key)+" "+str(self.doorNum))
        if self.doorNum == key:
            self.locked = False
            #print("Unlocked")
            return True
        return False
    def getDoorNum(self):
        return self.doorNum
    def getDoorDir(self):
        return self.direction
    def toString(self):
        retDesc = self.direction
        if(self.locked):
            retDesc = retDesc+" (locked, key#"+str(self.doorNum)+")"
        return retDesc
