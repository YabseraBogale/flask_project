from make_file import WordDatabase
import random

def giveRandomWord():
    test=WordDatabase()
    for i in range(0,100):
        num=random.randint(500,5000)
        word=test.seeWordWithId(num)
        print(f"Id:{num} word:{word}")
    return "passed"

def seeWordCount():
    test=WordDatabase()
    print(test.seeNumberOfWords()-1)

def seeLastWord():
    test=WordDatabase()
    print(test.seeWordWithId(10000))

print(seeLastWord())


