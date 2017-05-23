import random
from EnvironmentGenerator import *


class maze():

    def getSurrounding(self, curr):
        surr = []
        depth = self.height
        width = self.width
        above = None
        below = None
        left = None
        right = None

        if (curr.x + 1 < depth):
            above = self.matrix[curr.x + 1][curr.y];
        if (curr.x - 1 >= 0):
            below = self.matrix[curr.x - 1][curr.y];
        if (curr.y - 1 >= 0):
            left = self.matrix[curr.x][curr.y - 1];
        if (curr.y + 1 < width):
            right = self.matrix[curr.x][curr.y + 1];
        if (above != None and above.visited == False):
            # print(type(above))
            # print('above')
            surr.append(above);
        if (below != None and below.visited == False):
            # print(type(below))
            # print('below')
            surr.append(below);
        if (left != None and left.visited == False):
            # print(type(left))
            # print("left")
            surr.append(left);
        if (right != None and right.visited == False):
            # print(type(right))
            # print("right")
            surr.append(right);
        return surr;

    def buildMaze(self, start, end):
        st = []
        st.append(start)
        start.visited = True
        foundEnd = False
        curr = start
        while(len(st) > 0):
            surrVert = self.getSurrounding(curr)
            curr.visited = True
            if(len(surrVert) > 0):
                st.append(curr)

                curr = random.choice(surrVert)

                if(curr.x == st[-1].x):
                    if(curr.y < st[-1].y):
                        curr.right = False
                        st[-1].left = False
                    else:
                        curr.left = False
                        st[-1].right =  False
                else:
                    if (curr.x < st[-1].x):
                        curr.below = False;
                        st[-1].above = False;
                    else:
                        curr.above = False;
                        st[-1].below = False;
                if(not foundEnd):
                    if(curr == end):
                        foundEnd = True;
            else:
                curr = st.pop()

    def addDoors(self):
        up = 0
        down = 0
        left = 0
        right = 0
        for v in self.matrix:
            for z in v:
                if z.above == False:
                    up = 1
                if z.below == False:
                    down = 1
                if z.left == False:
                    left = 1
                if z.right == False:
                    right = 1
                z.environment = genEnvironment(self.difficulty,up,down,right,left)

    def getVertex(self,x,y):
        return self.matrix[x][y]

    def __init__ (self, height, width,difficulty):
        self.height = height
        self.width = width
        self.difficulty = difficulty
        self.matrix = [[0 for x in range(width)] for y in range(height)]

        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Vertex(i, j)
        start = self.matrix[0][0]
        end = self.matrix[self.height - 1][self.width - 1]

        start.above = False
        end.below = False

        self.buildMaze(start, end)
        self.addDoors()


# Vertex for the maze. The maze is represented as a graph
class Vertex():

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.above = True
        self.below = True
        self.left = True
        self.right = True
        self.visited = False
        self.environment = None
    def getEnv(self):
        return self.environment

