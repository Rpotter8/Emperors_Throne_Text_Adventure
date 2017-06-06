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
import time
import sys
import winsound
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("dungeon.wav")
#play_obj.wait_done()
Freq = 500 # Set Frequency To 2500 Hertz
Dur = 50 # Set Duration To 1000 ms == 1 second
#winsound.Beep(500,1000)


def dprint(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        #winsound.Beep(Freq,Dur)
        time.sleep(0.025)
    time.sleep(.3)
    print()

def thunder():
    wav = sa.WaveObject.from_wave_file("danger2.wav")
    play = wav.play()
    play.wait_done()
    time.sleep(.5)
    play = wav.play()
    play.wait_done()
    time.sleep(.15)
    play = wav.play()
    play.wait_done()


#Game Intro!
dprint("Welcome Player!")
name = input("Please Input Your Name! ")
#defaults to yes
stot = input("Would you like to use speech to text? y/n : ")
while True:
    try:
        difficulty = int(input("Please Select a Difficulty From 1-5 : "))
        if(difficulty>0 and difficulty<6):
            break
    except ValueError:
        print()
#Player initialization
#TODO modify stats based on difficulty
player = Player(name,100,2)
print("\n\n---------------------------------------------------------------------------------------------")
dprint("Welcome "+name+"! You are about to embark on a great quest which\n is a matter of life and death for the entire kingdom!")
dprint("Our story begins here:")




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
                    a@@@@@@@\   | `| ''.'     .' | ' /@@@@@@@@@a  
--------------------------------------------------------------------------------""")

thunder()
play_obj = wave_obj.play()
input("\n\tPress Enter to Continue...\n")
dprint("This is your father's castle. Yet your adventure does not start in the throne\nroom, or the dining room, or even your bedroom.")
input("\n\tPress Enter to Continue...\n")
dprint("You have awoken this morning locked in the jail cell in the cellar of the\ncastle. Surrounded by rats and other undesirables.")
input("\n\tPress Enter to Continue...\n")
dprint("Your memory slowly returns as you clear the sleep from your eyes...")
dprint("You remember the violent murder of your father at the hands of your uncle\nYou realize your uncle must have thrown you in the jail to keep you out of")
dprint("the way until he can fully take over the kingdom!")
input("\n\tPress Enter to Continue...\n")
dprint("You quickly escape the jail cell and decide to confront your uncle in the\nthrone room!")
input("\n\tPress Enter to Continue...\n")
#Game Starts Here!
#Predefined location, with one potion type random item.
CurrEnv = 0
currfloor = maze(5,5,difficulty)

#currfloor.display()
#JailCell = Environment([EnvironmentGenerator.genObject(2,difficulty)],"smelly dark room outside your jail cell",[Door(False,"Up",0)])
CurrEnv = currfloor.getVertex(player.getLocation()[1],player.getLocation()[0]).getEnv()
dprint(CurrEnv.toString())
#Testing RunCode
while(1):
    #print("y:"+str(player.getLocation()[0])+" x:"+str(player.getLocation()[1]))
    if not play_obj.is_playing():
        play_obj = wave_obj.play()
    print("\n")
    data = ""
    if(stot.lower() == 'y' or stot.lower() == 'yes'):
        text = RecognizeSpeech.recognize()
        data = InputProcessor.processInput(text,player,CurrEnv)
    else:
        data = InputProcessor.processInput(input("What do you do..?\n\t"),player,CurrEnv)
    if("Grab" in data):
        continue
    if("Inventory" in data):
        dprint("This is your inventory...\n")
        continue
    if("Equipment" in data):
        dprint("Those are your equipped items..\n")
        continue
    if("Equip" in data):
        dprint ("Equipping done.\n")
        continue
    if("Stairs" in data):
        currfloor = maze(5,5,++difficulty)
        player.setLocation(0,0)
        CurrEnv = currfloor.getVertex(player.getLocation()[1],player.getLocation()[0]).getEnv()
        dprint(CurrEnv.toString())
        continue
    if("Look" in data):
        dprint(CurrEnv.toString())
        continue
        #print("I do not understand your command")
    if("Fail" in data):
        continue
    if("Error" not in data and "Look" not in data):
        CurrEnv = currfloor.getVertex(player.getLocation()[1],player.getLocation()[0]).getEnv()
        dprint(CurrEnv.toString())
        continue    
    #This is not working
    if(data[5:] == " "):
        dprint(str("You must act, "+player.getName()+"!\n"))
        continue
    dprint(str("You "+data[5:]+", but nothing happens..\n"))
    #input("Press Enter to Continue...")
    #print(EnvironmentGenerator.genEnvironment(difficulty,"Up").toString())