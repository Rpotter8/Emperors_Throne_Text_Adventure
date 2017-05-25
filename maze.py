
import random
from EnvironmentGenerator import *

WALL = "X"

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
            below = self.matrix[curr.x + 1][curr.y];
        if (curr.x - 1 >= 0):
            above = self.matrix[curr.x - 1][curr.y];
        if (curr.y - 1 >= 0):
            left = self.matrix[curr.x][curr.y - 1];
        if (curr.y + 1 < width):
            right = self.matrix[curr.x][curr.y + 1];
        if (above != None and above.visited == False):
            # print(type(above))
            # print('above', end='')
            surr.append(above);
        if (below != None and below.visited == False):
            # print(type(below))
            # print('below', end='')
            surr.append(below);
        if (left != None and left.visited == False):
            # print(type(left))
            # print("left", end='')
            surr.append(left);
        if (right != None and right.visited == False):
            # print(type(right))
            # print("right", end='')
            surr.append(right);
        print()
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

        for v in self.matrix:

            for z in v:
                up = 0
                down = 0
                left = 0
                right = 0
                if z.above == False:
                    up = 1
                if z.below == False:
                    down = 1
                if z.left == False:
                    left = 1
                if z.right == False:
                    right = 1
                z.environment = genEnvironment(self.difficulty,up,down,right,left)
                if(z.x==0 and z.y==0):
                    z.environment.changeDesc("smelly dark room outside your jail cell")
                    z.environment.addItem(genObject(2,self.difficulty))
    def getVertex(self,x,y):
        return self.matrix[x][y]
    def display(self):

        height = len(self.printer)
        width = len(self.printer[0])

        for i in range(width):
            for j in range(height):
                print(self.printer[i][j], end='')
            print()
        for i in range(height):
            if(i == 0):
                for j in range(width):
                    if (not (j % 2 == 0) and not self.matrix[i][j // 2].above):
                        self.printer[i][j] = ' '
                    else:
                        self.printer[i][j] = WALL
            else:
                for j in range(width):
                    if(i % 2 == 0):
                        if(j % 2 == 0):
                            self.printer[i][j] = WALL
                        else:
                            if(self.matrix[i // 2 - 1][j // 2].below):
                                self.printer[i][j] = WALL
                            else:
                                self.printer[i][j] = ' '
                    else:
                        if (j % 2 == 0):
                            if (j < width - 1):
                                if (self.matrix[i // 2][j // 2].left):
                                    self.printer[i][j] = WALL
                                else:
                                    self.printer[i][j] = ' '
                            else:
                                if (self.matrix[i // 2][j // 2 - 1].right):
                                    self.printer[i][j] = WALL
                                else:
                                    self.printer[i][j] = ' '
                        else:
                            if (self.matrix[i // 2][j // 2]):
                                self.printer[i][j] = ' '
                            else:
                                self.printer[i][j] = ' '
        for i in range(width):
            for j in range(height):
                print(self.printer[i][j], end='')
            print()


    def __init__ (self, height, width, difficulty):
        self.height = height
        self.width = width

        self.difficulty = difficulty
        self.matrix = [[0 for x in range(self.width)] for y in range(self.height)]
        self.printer = [[0 for x in range(self.width*2 + 1)] for y in range(self.height*2 + 1)]

        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Vertex(i, j)
        start = self.matrix[0][0]
        end = self.matrix[self.height - 1][self.width - 1]



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



# maze(5,5,1).display()
