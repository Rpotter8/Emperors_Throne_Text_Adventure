#Emperor's Throne Pre-Alpha 0.0.01
#Game Core
import Entity
import random
import Environment
import EnvironmentGenerator

#Game Intro!
print("Welcome Player!")
name = input("Please Input Your Name! ")
difficulty = int(input("Please Select a Difficulty From 1-5 "))
print("---------------------------------------------------------------------------------------------")
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
input("Press Enter to Continue...")
print("This is your father's castle. Yet your adventure does not start in the throne room, or the dining room, or even your bedroom.")
input("Press Enter to Continue...")
print("You have awoken this morning locked in the jail cell in the cellar of the castle. Surrounded by rats and other undesirables.")
input("Press Enter to Continue...")
print("Your memory slowly returns as you clear the sleep from your eyes...")
print("You remember the violent murder of your father at the hands of your uncle\nYou realize your uncle must have thrown you in the jail to keep you out of the way")
print("until he can fully take over the kingdom!")
print("Press Enter to Continue...")
print("You quickly escape the jail cell and decide to confront your uncle in the throne room!")
input("Press Enter to Continue...")
#Game Starts Here!
JailCell = Environment([Entity("Non-descript Potion","Potion",0,5)],"smelly dark room outside your jail cell.")
print(JailCell.toString())

#Testing RunCode
#while(1):
#    input("Press Enter to Continue...")
#    print(EnvironmentGenerator.genEnvironment(difficulty).toString())

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
