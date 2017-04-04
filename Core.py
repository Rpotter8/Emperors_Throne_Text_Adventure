#Emperor's Throne Pre-Alpha 0.0.01
#Game Core
from Entity import *
import random
from Environment import *

#Game Intro!
print("Welcome Player!")
name = input("Please Input Your Name! ")
difficulty = int(input("Please Select a Difficulty From 1-5"))
print("Welcome "+name+"! You are about to embark on a great quest which\n is a matter of life and death for the entire kingdom!")
print("Our story begins here:")
print("""
          ___     ___     ___     ___          ___     ___     ___     ___
         |   |   |   |   |   |   |   |        |   |   |   |   |   |   |   |
         |   |   |   |   |   |   |   |        |   |   |   |   |   |   |   |
         |   |___|   |___|   |___|   |________|   |___|   |___|   |___|   |
         |                                                                |
         |            ___                                  ___            |
         |           /   \                                /   \           |
         |          |     |                              |     |          |
         |          |     |                              |     |          |
         |          |_____|                              |_____|          |
         |                        __________________                      |
         |                       /  |  |      |  |  \                     |
         |                      /   |  |      |  |   \                    |
         |                     /    |  |      |  |    \                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |     |  |      |  |    |                   |
         |                    |_____|__|______|__|____|                   |""")

#Testing RunCode

#objects = []
#for i in range(0,10):
#    generate = random.randint(0,2)
#    Object = ""
#    if(generate == 0):
#        generate1 = random.randint(0,10)
#        generate2 = random.randint(0,10)
#        Object = Entity("Dragon","Enemy",generate1,generate2)
#    elif(generate == 1):
#        generate1 = random.randint(0,10)
#        Object = Entity("Silver Key","Key",generate1,0)
#    else:
#        generate1 = random.randint(0,10)
#        generate2 = random.randint(0,10)
#        Object = Entity("Potion","Potion",generate1,generate2)
#    objects.append(Object)
#cEnvironment = Environment(objects,"a small room")
#print(cEnvironment.toString())
