import sqlite3
import keyword
import random
import os
class WordDatabase():
    def __init__(self):
        self.connect=sqlite3.Connection('word.db')
        self.pointer=self.connect.cursor()
    # the data inserted int run is tuple
    def run(self,data):
        stat="insert into word(ID,word) values(?,?)"
        self.pointer.execute(stat,data)
        self.connect.commit()
        return "Done"
    def insertTablePython(self):
        stat="insert INTO Python(ID,Pword)values(?,?)"
        lst=self.giveMostPythonKeyWord()
        for i in lst:
            self.pointer.execute(stat,(lst.index(i),i))
            self.connect.commit()
        return "Done"
    def pythonKeyword(self):
        self.lst=keyword.kwlist
        return self.lst
    def pythonSymbol(self):
        self.symbol=["+","-","*","**","/","//","%","<<",">>","&","|","^","~","<",">",
                        "<=",">=","==","!=","<>","+=","-=","*=","/=","//=","%=","**=","&=","|=","^=",">>=","<<="
                        "(",")","[","]","{","}",",",":",".","`","=",";","'","#","@","'\'"
                    ]
        return self.symbol
    def creatTableWordList(self):
        stat="""
            create table word(
                ID int not null,
                word varchar(30) not null
            );

        """
        self.pointer.execute(stat)
        self.connect.commit()
        return "Done"
    def createTablePython(self):
        stat="""
            create table Python(
                ID int not null primary key ,
                Pword varchar(30) not null unique
            );
        """
        self.pointer.execute(stat)
        self.connect.commit()
        return "Done"
    def seeNumberOfWords(self):
        stat="select count(Id) from word;"
        self.pointer.execute(stat)
        self.result=self.pointer.fetchone()
        return int(self.result[0])
    def seeAll(self):
        stat="select ID,word from word"
        self.pointer.execute(stat)
        self.result=self.pointer.fetchall()
        for i in self.result:
            print(f"ID:{i[0]} word:{i[1]}")
        return "Done"
    def seeWordWithId(self,ID):
        stat="select word from word where word.ID=(?)"
        self.pointer.execute(stat,(ID,))
        self.result=self.pointer.fetchone()
        return self.result[0]
    def seeIDWithWord(self,word):
        stat="select ID from word where word.word=(?)"
        self.pointer.execute(stat,(word,))
        self.result=self.pointer.fetchone()
        return self.result[0]
    def readFile(self,fileName):
        file=open(fileName)
        j=1
        for i in file.readlines():
            self.run((j,i.strip()))
            print(f"step taking {j}")
            j+=1
        return "Done"
    def getAll(self):
        stat="select ID,word from word"
        self.pointer.execute(stat)
        self.result=self.pointer.fetchall()
        return self.result
    def giveMostPythonKeyWord(self):
        self.lst=self.pythonSymbol()+self.pythonKeyword()
        return self.lst
    def seeMostPythonKeyWord(self):
        stat="select ID,Pword FROM Python"
        self.pointer.execute(stat)
        self.result=self.pointer.fetchall()
        print(len(self.result))
        for i in self.result:
            print(f"ID {i[0]} KeyWord:{i[1]}")
        return "Done"
    def giveMeLengthOfWordGiveYouFile(self,length):
        lst=[]
        commit_files=os.getcwd()+'/commit_files'
        fileName=self.seeWordWithId(random.randint(1,10000))+".json"
        if not os.path.exists(commit_files):
            os.mkdir(commit_files)
        filePath=os.path.join(commit_files,fileName)
        for i in range(0,length):
            lst.append(self.seeWordWithId(random.randint(1,10000)))
        file=open(filePath,"a")
        file.write(str(lst))
        file.close()
        return "Check in ./commit_files"
    def closeDatabase(self):
        self.connect.close()
        return "closed"
    
