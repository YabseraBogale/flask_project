from word_database import WordDatabase
import os
import time
from time import sleep
import random

class Commit():
    def __init__(self):
        self.database=WordDatabase()

    def howManyFilesAndNumberOfWord(self,fileNumber,fileLength):
        for i in range(0,fileNumber):
            print(f"setps taking {i+1}")
            self.database.giveMeLengthOfWordGiveYouFile(fileLength)
        return "Done"
    
    def gitcommit(self,msg,number_of_time_runnig):
        print(os.system("git status"))
        print(os.system("git add ."))
        print(os.system(f"git commit -m '{msg}'"))
        print(os.system("git push"))
        print(f"Number of commit is at {number_of_time_runnig}")
    
    def onlyGitCommit(self):
        self.status=os.system("git status")
        if self.status==0:
            os.system("git add .")
            os.system("git commit -m 'ok'")
            os.system("git push")
            return "git pushed"
        return "check it ?"                     
  
    def giveMeCommitNumber(self,numberOfCommit):
        for i in range(0,numberOfCommit):
            self.howManyFilesAndNumberOfWord(1,100)
            msg=self.database.seeWordWithId(random.randint(0,500))
            self.gitcommit(msg,i)
        self.database.closeDatabase()
        return "Done"
