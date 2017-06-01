import nltk

file = open("clean.txt")

while(1):
    nb = input("Enter a sentence: ")
    nb = nltk.word_tokenize(nb)
    nb = nltk.pos_tag(nb)
    print(str(nb))
