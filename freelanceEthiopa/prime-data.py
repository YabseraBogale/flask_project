import sqlite3
class TableCreate():

    def __init__(self) -> None:
        self.connection=sqlite3.Connection("prime-data.db")
        self.pointer=self.connection.cursor()
    
    def CreateTelegramChannelTable(self,telegramchannelname) -> str:
        statment="""
                create table ?(
                    CompanyName varchar(20) not null,
                    RequestData datetime not null,
                    Location varchar(20) not null,
                    JobPosition varchar(20) not null,
                    Salary float not null,
                    Phone int not null,
                    Email varchar(20) not null
                );
            """
        self.pointer.execute(statment,(telegramchannelname,))
        self.connection.commit()
        return "done"
    
    def InsertIntoTable(self,tablename,companyname,requestdata,location,jobposition,salary,phone,email) -> str:
        statment="insert into ?(CompanyName,RequestData,Location,JobPosition,Salary,Phone,Email) values(?,?,?,?,?,?,?,?)"
        self.pointer.execute(statment,(tablename,companyname,requestdata,location,jobposition,salary,phone,email,))
        self.connection.commit()
        return "done"
    
    def SeeInTable(self,tablename) -> tuple:
        statment="select * from ?"
        self.pointer.execute(statment,(tablename,))
        result=self.pointer.fetchall()
        return result

    def CloseConnection() ->str:
        self.connection.closed()
        return "Connection closed"


    def DropTable(self,name) ->str:
        statment="drop table ?"
        self.pointer.execute(statment,(name,))
        return f"Droped table {name}"
