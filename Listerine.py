from random import *
from time import *
wordlist = open("wordlist.txt","r")
thelist = [1, 12, 123, 1234, 12345, 123456]
thelistofstrings = ["auchnichtaufdembalkon", "dasteerdachbrenntzuschnellab", "erwinhuepfer", "memememememe", "olebacktnenkuchen", "Zeileistvielzulang"]
thelistoftuples = [(1, 1), (2, 3), (5, 6)]
thelistoflits = [[1, 2, 3, 4], ["diesezeilewirdauchvielzulang", "und wenn ich whitespace benutzen muss!"], ["Na also, sag´ ich doch!", "3Distüberbewertet"]]
for x in range(1, 100):
    print(100*"-")
    print("cycle", x)
    print("random floating point:", random())
    print("random integer between 23 and 1337: ", randint(23, 1337))
    #print(shuffle(thelist)) # Y dis no Work? Merely returns "None"
    shuffle(thelist)
    print("shuffled List: ", thelist)
    simplesample = sample(thelist, 1)
    print("Random sample from List: ", simplesample)
    multisample = sample(thelist, 3)
    print(multisample)
    print(sample(thelistofstrings, 1))
    #print(sample(wordlist, 1)) #probably something wrong with the wordlist formatting. No Clue what, though. Running Debugger on the wordlists Value in Line 3 might prove insightful. This Line is way too long, BTW.
    sleep(0.2)
