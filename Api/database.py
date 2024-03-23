import sqlite3
class Database():
    def __init__(self):
        self.connection=sqlite3.Connection("MainDatabase.db")
        self.pointer=self.connection.cursor()

    def CreateTable(self):
        statment="create table IF NOT EXISTS CompanyInformation( companyname varchar(80) not null, telegramchannel varchar(20) not null, title varchar(30) not null,date datetime not null,location(50) not null, stack json )"
        self.pointer.execute(statment)
        self.connection.commit()
        statment="create table IF NOT EXISTS MetaData( nameofchannel varchar(80) not null, sizeofdataset int not null, foundjob int not null, perectange float not null )"
        self.pointer.execute(statment)
        self.connection.commit()
        return "Sucessfully made table"

    def InsetIntoCompanyInformation(self,name,telegramchannel,title,date,location,stack):
        statment="insert into CompanyInformation(companyname,telegramchannel,title,date,location,stack) values(?,?,?,?,?,?)"
        self.pointer.execute(statment,(name,telegramchannel,title,date,location,stack))
        self.connection.commit()
        return "Sucessfully inserted into table Company infromation"

    def InsertIntoMetaData(self,nameofchannel,sizeofdataset,foundjob,perectange):
        statment="insert into MetaData(nameofchannel,sizeofdataset,foundjob,perectange) values(?,?,?,?)"
        self.pointer.execute(statment,(nameofchannel,sizeofdataset,foundjob,perectange))
        self.connection.commit()
