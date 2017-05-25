import re

def cleanFile(file_name):
	clean = open('clean.txt', 'w')
	with open(file_name) as dirt:
		text=dirt.read().replace('\n', ' ')
		#text = re.sub(r"([^a-zA-Z']*(?=[^a-zA-Z']))"," ",text)
		text = re.sub(r"([^a-zA-Z\.\;'])"," ",text)
		text = re.sub(r"([\.]+)",".",text)
		text = ' '.join(word for word in text.split() \
			if (len(word)>1 or word.lower() == 'a' or word.lower() == 'i')\
			and len([l for l in word if l.isupper()]) <= 1)
		text=text.replace('.','.\n')
		clean.write(text)

cleanFile('dirty.txt')