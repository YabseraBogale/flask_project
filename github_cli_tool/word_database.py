import sqlite3
import keyword
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
    def pythonKeyword(self):
        self.lst=keyword.kwlist
        return self.lst
    def pythonSymbol(self):
        self.symbol=["+","-","*","**","/","//","%","<<",">>","&","|","^","~","<",">",
                        "<=",">=","==","!=","<>","+=","-=","*=","/=","//=","%=","**=","&=","|=","^=",">>=","<<="
                        "(",")","[","]","{","}",",",":",".","`","=",";"
                    ]
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
    def getFile(self):

    


