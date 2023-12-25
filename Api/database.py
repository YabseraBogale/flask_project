import sqlite3
class Database():
    def __init__(self):
        self.connection=sqlite3.Connection("MainDatabase.db")
        self.pointer=self.connection.cursor()
    
    def CreateTable(self):
        statment="create table IF NOT EXISTS TechStack( id int not null primary key, filename varchar(20) not null )"
        self.pointer.execute(statment)
        self.connection.commit()
        statment="create table IF NOT EXISTS CompanyInformation( companyname varchar(80) not null, telegramchannel varchar(20) not null, title varchar(30) not null,date datetime not null,location(50) not null, techstackid int not null )"
        self.pointer.execute(statment)
        self.connection.commit()

    def InsertIntoTechStack(self,filename)
