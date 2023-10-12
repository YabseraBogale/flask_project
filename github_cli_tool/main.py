from word_database import WordDatabase
import os
import sys
import random

class Commit():
    def __init__(self):
        self.database=WordDatabase()

    def howManyFilesAndNumberOfWord(self,fileNumber,fileLength):
        for i in range(0,fileNumber):
            print(f"setps taking {i+1}")
            self.database.giveMeLengthOfWordGiveYouFile(fileLength)
        return "Done"
    
    def gitcommit(self,msg):
        print(os.system("git status"))
        print(os.system("git add ."))
        print(os.system(f"git commit -m '{msg}'"))
        print(os.system("git push"))

    def giveMeCommitNumber(self,numberOfCommit):
        for i in range(0,numberOfCommit):
            self.howManyFilesAndNumberOfWord(1,100)
            msg=self.database.seeWordWithId(random.randint(0,500))
            self.gitcommit(msg)
            print(f"Number of commit is at {i}")
        self.database.closeDatabase()
        return "Done"
