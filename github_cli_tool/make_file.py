import sqlite3

class WordDatabase():
    #self.connect=sqlite3.Connection('word.db')
    #self.pointer=self.connect.cursor()
    pass

# the data inserted int run is tuple
def run(data):
    connect=sqlite3.Connection('word.db')
    pointer=connect.cursor()
    stat="insert into word(ID,word) values(?,?)"
    pointer.execute(stat,data)
    connect.commit()
    return "Done"


def seeLast():
    df=pd.read_sql()

def seeNumberOfWords():
    connect=sqlite3.Connection('word.db')
    pointer=connect.cursor()
    stat="select count(Id) from word;"
    pointer.execute(stat)
    result=pointer.fetchone()
    return result[0]

def seeAll():
    connect=sqlite3.Connection('word.db')
    pointer=connect.cursor()
    stat="select ID,word from word"
    pointer.execute(stat)
    result=pointer.fetchall()
    for i in result:
        print(f"ID:{i[0]} word:{i[1]}")
    return "Done"

def seeWordWithId(ID):
    connect=sqlite3.Connection('word.db')
    pointer=connect.cursor()
    stat="select word from word where word.ID=(?)"
    pointer.execute(stat,(ID,))
    result=pointer.fetchone()
    return result[0]

def seeIDWithWord(word):
    connect=sqlite3.Connection('word.db')
    pointer=connect.cursor()
    stat="select ID from word where word.word=(?)"
    pointer.execute(stat,(word,))
    result=pointer.fetchone()
    return result[0]


def readFile():
    file=open('words.txt')
    k=10000
    j=1
    for i in file.readlines():
        run((j,i.strip()))
        j+=1
        k-=1
        print(f"setp taking {k}")
    return "Done"

print(readFile())
