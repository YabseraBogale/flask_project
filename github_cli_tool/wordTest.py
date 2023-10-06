from word_database import WordDatabase
import random
import sqlite3
import os

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

def create_table():
    stat="""
        create table word(
            ID int not null primary key ,
            word varchar(30) not null unique
        );
    """
    connect=sqlite3.Connection('test.db')
    pointer=connect.cursor()
    pointer.execute(stat)
    connect.commit()
    return "Done"

def createTablePython():
    stat="""
        create table Python(
            ID int not null primary key ,
            Pword varchar(30) not null unique
        );
    """
    connect=sqlite3.connect('test.db')
    pointer=connect.cursor()
    pointer.execute(stat)
    connect.commit()
    return "Done"

def insertTablePython():
    stat="insert INTO Python(ID,Pword)values(?,?)"
    connect=sqlite3.connect('test.db')
    pointer=connect.cursor()
    test=giveMostPythonKeyWord()
    for i in test:
        pointer.execute(stat,(test.index(i),i))
        connect.commit()
    return "Done"

def seeMostPythonKeyWord():
    stat="select ID,WORD FROM Python"
    connect=sqlite3.connect('test.db')
    pointer=connect.cursor()
    pointer.execute(stat)
    result=pointer.fetchall()
    for i in result:
        print(f"ID {i[0]} KeyWord:{i[1]}")
    return "Done"

def giveMostPythonKeyWord():
    test=WordDatabase().pythonSymbol()+WordDatabase().pythonKeyword()
    return test


def howManyFilesAndNumberOfWord(fileNumber,fileLength):
    test=WordDatabase()
    for i in range(0,fileNumber):
        test.giveMeLengthOfWordGiveYouFile(fileLength)
    return "Done"



def insertData():
    stat="insert into word(ID,word) values(?,?);"
    connect=sqlite3.Connection('test.db')
    pointer=connect.cursor()
    pointer.execute(stat,(5,"hello",))
    connect.commit()
    return "Done"


print()



