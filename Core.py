#Emperor's Throne Pre-Alpha 0.0.5
#Game Core
from Entity import *
import random
from Environment import *
from Player import *
from Door import *
import EnvironmentGenerator
import InputProcessor
import RecognizeSpeech
from maze import *

#Game Intro!
print("Welcome Player!")
name = input("Please Input Your Name! ")
#defaults to yes
stot = input("Would you like to use speech to text? y/n")
while True:
    try:
        difficulty = int(input("Please Select a Difficulty From 1-5 "))
        if(difficulty>0 and difficulty<6):
            break
    except ValueError:
        print()
#Player initialization
#TODO modify stats based on difficulty
player = Player(name,25,5)
print("\n\n---------------------------------------------------------------------------------------------")
print("Welcome "+name+"! You are about to embark on a great quest which\n is a matter of life and death for the entire kingdom!")
print("Our story begins here:")




print("""
                         _____ _   _ _____
              .     ..  |_   _| | | |  ___|          *
     .       -*           | | | |_| | |__      .             .
              |           | | |  _  |  __|     :-      .
     .:               .   | | | | | | |___          ..
                          \_/ \_| |_\____/           *            .""")
print (""" .     -*-                                 ..
	 ________  ________ ___________ ___________ _ _____
  .	|  ___|  \/  | ___ \  _  | ___ \  ___| ___ ( )  ___|	.
	| |__ | .  . | |_/ / | | | |_/ / |__ | |_/ //\ `--. 	*
   .	|  __|| |\/| |  __/| | | |    /|  __||    /   `--. \\
	| |___| |  | | |   \ \_/ / |\ \| |___| |\ \  /\__/ /  .
 .   .	\____/\_|  |_|_|    \___/\_| \_\____/\_| \_| \____/.""")

print("""		.		.:			.                  :
	         _____ _   _______ _____ _   _ _____
	   .    |_   _| | | | ___ \  _  | \ | |  ___| :.    .          ..
 :	          | | | |_| | |_/ / | | |  \| | |__          :
-*-	          | | |  _  |    /| | | | . ` |  __|              |
 :	      .   | | | | | | |\ \\\\ \_/ / |\  | |___   .         -*-
	          \_/ \_| |_|_| \_|\___/\_| \_|____/              :
	       .                  .           -*-     .:
  "       *                 ..                                 .        *
                         :                                .        .
       .         .      /\      .:  *       .          .              .
                 *    .'  `.      .     .     *      .                  .
  :             .    /      \  _ .________________  .                    .
       |            `.+-~~-+.'/.' `.^^^^^^^^\~~~~~\.                      .
 .    -*-   . .       |u--.|  /     \~~~~~~~|~~~~~|
       |              |   u|.'       `.\" \"  |\" \" \"|                        .
    :            .    |.u-./ _..---.._ \\\" \" | \" \" |
   -*-            *   |    ~-|U U U U|-~____L_____L_                      .
    :         .   .   |.-u.| |..---..|\"//// ////// /\       .            .
          .  *        |u   | |       |// /// // ///==\     / \          .
 .          :         |.--u| |..---..|//////~\////====\   /   \       .
      .               | u  | |       |~~~~/\\u |~~|++++| .`+~~~+'  .
                      |.-|~U~U~|---..|u u|u | |u ||||||   |  U|
                   /~~~~/-\---.'     |===|  |u|==|++++|   |   |
          aaa      |===| _ | ||.---..|u u|u | |u ||HH||U~U~U~U~|        aa@@@@
     aaa@@@@@@aa   |===|||||_||      |===|_.|u|_.|+HH+|_/_/_/_/aa    a@@@@@@@@
 aa@@@@@@@@@@@@@@a |~~|~~~~\---/~-.._|--.---------.~~~`.__ _.@@@@@@a    ~~~~~~
   ~~~~~~    ~~~    \_\\\\ \  \/~ //\  ~,~|  __   | |`.   :||  ~~~~
                     a\`| `   _//  | / _| || |  | `.'  ,''|     aa@@@@@@@a
 aaa   aaaa       a@@@@\| \  //'   |  // \`| |  `.'  .' | |  aa@@@@@@@@@@@@@a
@@@@@a@@@@@@a      ~~~~~ \\\\`//| | \ \//   \`  .-'  .' | '/      ~~~~~~~  ~~
@@@@@@@@@@@@@@@a          \// |.`  ` ' /~  :-'   .'|  '/~aa
~~~~~~~ ~~~~~~         a@@@|   \\\\ |   // .'    .'| |  |@@@@@@a
                    a@@@@@@@\   | `| ''.'     .' | ' /@@@@@@@@@a  """)


input("Press Enter to Continue...")
print("This is your father's castle. Yet your adventure does not start in the throne room, or the dining room, or even your bedroom.")
input("Press Enter to Continue...")
print("You have awoken this morning locked in the jail cell in the cellar of the castle. Surrounded by rats and other undesirables.")
input("Press Enter to Continue...")
print("Your memory slowly returns as you clear the sleep from your eyes...")
print("You remember the violent murder of your father at the hands of your uncle\nYou realize your uncle must have thrown you in the jail to keep you out of the way")
print("until he can fully take over the kingdom!")
input("Press Enter to Continue...")
print("You quickly escape the jail cell and decide to confront your uncle in the throne room!")
input("Press Enter to Continue...")
#Game Starts Here!
#Predefined location, with one potion type random item.
CurrEnv = 0
currfloor = maze(5,5,difficulty)
#currfloor.display()
#JailCell = Environment([EnvironmentGenerator.genObject(2,difficulty)],"smelly dark room outside your jail cell",[Door(False,"Up",0)])
CurrEnv = currfloor.getVertex(player.getLocation()[0],player.getLocation()[1]).getEnv()
print(CurrEnv.toString())
#Testing RunCode
while(1):
    print("x:"+str(player.getLocation()[0])+" y:"+str(player.getLocation()[1]))
    data = ""
    if(stot != 'n'):
        text = RecognizeSpeech.recognize()
        data = InputProcessor.processInput(text,player,CurrEnv)
    else:
        data = InputProcessor.processInput(input("What do you do?"),player,CurrEnv)
    if("Grab" in data):
        print("GRABBY GRABBY")
    if("Error" not in data and "Look" not in data):
        CurrEnv = currfloor.getVertex(player.getLocation()[0],player.getLocation()[1]).getEnv()
        print(CurrEnv.toString())
        continue
    if("Look" in data):
        print(CurrEnv.toString())
        continue
        #print("I do not understand your command")
    #This is not working
    if(data[5:] == " "):
        print("You must act, Adventurer!")
        continue
    print("You "+data[5:]+", but nothing happens")
    #input("Press Enter to Continue...")
    #print(EnvironmentGenerator.genEnvironment(difficulty,"Up").toString())
