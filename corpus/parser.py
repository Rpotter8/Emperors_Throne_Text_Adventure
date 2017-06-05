import nltk
from nltk.corpus import wordnet

file = open("clean.txt")

while(1):
    nb = input("Enter a sentence: ")
    nb = nltk.word_tokenize(nb)
    nb = nltk.pos_tag(nb)
    print(nb)

    verb = None
    action = None
    for i in nb:
        if(i[1] == "VBP" or i[1] == "VBD"):
            verb = i[0]
        if(i[1] == "RB" or i[1] == "RP" or i[1] == "NNS" or
            i[1] == "NN"):
            action = i[0]
        if(verb != None and action != None):
            print("Verb: " + verb +", Action: " + action)
            break


    
