from __future__ import print_function
import random



class maze():

    def getSurrounding(self, curr):
        print(type(curr))
        print(str(curr.x) + "|" + str(curr.y) + "\n")
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
        for i in surr:
            print(str(i.x) + " " + str(i.y))
        print("\n")
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





    def __init__ (self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[0 for x in range(width)] for y in range(height)]

        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Vertex(i, j)
        start = self.matrix[0][0]
        end = self.matrix[self.height - 1][self.width - 1]

        start.above = False
        end.below = False

        self.buildMaze(start, end)



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


blah = maze(5,5)

for i in range(5):
    for j in range(5):
        print(str(blah.matrix[i][j].x) + ", " + str(blah.matrix[i][j].y) + ' | ', end='')
    print('\n')
