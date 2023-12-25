import sqlite3
class Search():

    def __init__(self):
        self.connection=sqlite3.Connection("Search.db")
        self.pointer=self.connection.cursor()

    def CreateTable(self):

        statment="create table IF NOT EXISTS SearchTermTitle( title varchar(30) not null);"
        self.pointer.execute(statment)
        self.connection.commit()

        statment="create table IF NOT EXISTS SearchTermCompanyName( companyname varchar(80) not null);"
        self.pointer.execute(statment)
        self.connection.commit()

        statment="create table IF NOT EXISTS SearchTermLocation( location varchar(50) not null );"
        self.pointer.execute(statment)
        self.connection.commit()

        statment="create table IF NOT EXISTS SearchTermTechStack( stack varchar(15) not null );"
        self.pointer.execute(statment)
        self.connection.commit()

        return "Table Created"

    def InsertIntoSearchTermTitle(self,title):
        statment="insert into SearchTermTitle(title) values(?)"
        self.pointer.execute(statment,(title,))
        self.connection.commit()
        return f"Successfully into SearchTermTitle: {title}"

    def InsertIntoSearchTermCompanyName(self,companyname):
        statment="insert into SearchTermCompanyName(companyname) values(?)"
        self.pointer.execute(statment,(companyname,))
        self.connection.commit()
        return f"Successfully into earchTermCompanyName: {companyname}"

    def InsertIntoSearchTermLocation(self,location):
        statment="insert into SearchTermLocation(location) values(?);"
        self.pointer.execute(statment,(location,))
        self.connection.commit()
        return f"Successfully into SearchTermLocation: {location}"

    def InsertIntoSearchTermTechStack(self,stack):
        statment="insert into SearchTermTechStack(stack) values(?)"
        self.pointer.execute(statment,(stack))
        self.connection.commit()
        return f"Added {stack} to Database"

    def SearchForInTitleEnd(self,term):
        statment="select title from SearchTermTitle where title ;"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result
    
    def GetAllSearchTermLocation(self):
        statment="select * from SearchTermLocation"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result
    
    def GetAllSearchTermCompanyName(self):
        statment="select companyname from SearchTermCompanyName"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result
    
    def GetAllSearchTermTitle(self):
        statment="select title from SearchTermTitle"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result

    def IsTitleInSearchTerm(self,title):
        statment="select title from SearchTermTitle where title=?"
        self.pointer(statment,(title,))
        result=self.pointer.fetchall()
        return result

    def IsCompanyNameInSearchTerm(self,companyname):
        statment="select companyname from SearchTermCompanyName where=?"
        self.pointer(statment,(companyname,))
        result=self.pointer.fetchall()
        return result
    
    def DropSearchTermLocation(self):
        statment="drop table SearchTermLocation"
        self.pointer.execute(statment)
        self.connection.commit()
        return "Dropped table SearchTermLocation"

    def DropSearchTermTechStack(self):
        statment="drop table SearchTermTechStack"
        self.pointer.execute(statment)
        self.connection.commit()
        return "Dropped table SearchTermTechStack"

    def CloseConnection(self):
        self.connection.close()
        return "Connection Closed"


app=Search()

app.CreateTable()

from stack import Stack

stack = Stack().GiveTechStack()

for i in stack:
    print(app.InsertIntoSearchTermTechStack(i))
