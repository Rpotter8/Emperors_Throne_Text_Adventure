# Gabriel Summers


import random
import subprocess
from pygsr import Pygsr
#text = '"Hello world"'
#subprocess.call('espeak '+text)

class Player:
	def __init__(self):
		self.name = 'prisoner'
		self.items = ['health potion', 'bomb']
		self.health = 10
		self.weapon = 'dagger'
		self.armor = 8

	def printAll(self):
		desc =  ''.join(['My name is ',\
					   	 self.name,\
					     '.\nI am weilding a ',\
					     self.weapon,\
					     '.\nI have ',\
					     str(self.health),\
					     ' health left and ',\
					     str(self.armor),\
					     ' armor.\nI have ',\
					     str(len(self.items)),\
					     ' items.\n'])
		print(desc)
		if len(self.items) > 0:
			print('They are: ', self.items)



myself = Player() 
speech = Pygsr()

monsters 	= 	['spider','troll','bandit','slime','skeleton','zombie','goblin']
monDesc 	= 	['hairy','aggressive','large','smelly','rotted','evil','angry',\
		   	 	 'confused','scary','badass','hungry','fancy']
roomDesc	= 	['cold','empty','bright','cluttered','warm','stinky','fancy',\
				 'dark']
roomLocation=	['floor','table','rug']
roomItem	=	['chest','sword','bag of gold','gem','scroll','book','mask']

def generateTxt():
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



	output = ''.join(['"\nYou enter the ',\
					 random.choice(roomDesc),\
					 ' room and see a ',\
					 random.choice(roomItem),\
					 ' on the ',\
					 random.choice(roomLocation),\
					 '.\nIn the corner you see a ',
					 random.choice(monDesc),
					 ' ',
					 random.choice(monsters),
					 '\n\n... What do you do?\n\n"'])
	print(output)
	subprocess.call('espeak '+output)
	#speech.record(5)
	#phrase, complete_response = speech.speech_to_text('en_US')
	subprocess.call('python -m speech_recognition')
	#print (phrase)

def start():
	myself.printAll()

generateTxt()
start()
