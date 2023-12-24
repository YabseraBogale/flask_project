import sqlite3
class Prime():
    def __init__(self):
        self.connection=sqlite3.Connection("prime.db")
        self.pointer=self.connection.cursor()

    def CreateTable(self):
        statment="create table IF NOT EXISTS SearchTermTitle( title varchar(30) not null);"
        self.pointer.execute(statment)
        self.connection.commit()
        statment="create table IF NOT EXISTS SearchTermCompanyName( companyname varchar(80) not null);"
        self.pointer.execute(statment)
        self.connection.commit()
        return "Table Created"

    def InsertIntoSearchTermTitle(self,title):
        statment="insert into SearchTermTitle(title) values(?)"
        self.pointer.execute(statment,(title,))
        self.connection.commit()
        return f"Successful into Title: {title}"

    def InsertIntoSearchTermCompanyName(self,companyname):
        statment="insert into SearchTermCompanyName(companyname) values(?)"
        self.pointer.execute(statment,(companyname,))
        self.connection.commit()
        return f"Successful into Company Name: {companyname}"

    def AllGetCompanyName(self):
        statment="select companyname from SearchTermCompanyName"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result

    def SearchForInTitleEnd(self,term):
        statment="select title from SearchTermTitle where title ;"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result

    def AllGetTitle(self):
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


