import sqlite3
class Prime():
    def __init__(self):
        self.connection=sqlite3.Connection("prime.db")
        self.pointer=self.connection.cursor()
    def CreateTable(self):
        statment="create table IF NOT EXISTS create table SearchTermTitle( title varchar(30) not null);"
        self.pointer.execute(statment)
        self.connection.commit()
        statment="create table IF NOT EXISTS create table SearchTermCompanyName( companyname varchar(80) not null);"
        self.pointer.execute(statment)
        self.connection.commit()
        return "Table Created"
    def InsertIntoSearchTerm(self,title,companyname):
        statment="insert into SearchTermTitle(title) values(?)"
        self.pointer.execute(statment,(title,))
        self.connection.commit()
        statment="insert into SearchTermCompanyName(companyname) values(?)"
        self.pointer.execute(statment,(companyname,))
        self.connection.commit()
        return f"Successful Inserted title: {title} name: {companyname}"
    def AllGetCompanyName(self):
        statment="select companyname from SearchTermCompanyName"
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




test=Prime()
test.CreateTable()
