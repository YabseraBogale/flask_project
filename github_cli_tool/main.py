from word_database import WordDatabase
import os
import sys


class Commit():
    def __init__(self):
        self.database=WordDatabase()
    def howManyFilesAndNumberOfWord(self,fileNumber,fileLength):
        for i in range(0,fileNumber):
            print(f"setps taking {i+1}")
            self.database.giveMeLengthOfWordGiveYouFile(fileLength)
        return "Done"