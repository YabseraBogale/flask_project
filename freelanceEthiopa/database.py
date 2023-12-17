from pprint import pprint
import sqlite3
class TableCreate():

    def __init__(self) -> None:
        self.connection=sqlite3.Connection("prime-data.db")
        self.pointer=self.connection.cursor()
    
    def CreateTelegramChannelTable(self,telegramchannelname) -> str:
        statment=f"""
                CREATE TABLE IF NOT EXISTS {telegramchannelname} (
                    CompanyName varchar(20) not null,
                    RequestData datetime not null,
                    Location varchar(20) not null,
                    JobPosition varchar(20) not null,
                    Salary float not null,
                    Phone int not null,
                    Email varchar(20) not null
                );
            """
        self.pointer.execute(statment)
        self.connection.commit()
        return "done"
    
    def InsertIntoTable(self,tablename,companyname,requestdata,location,jobposition,salary,phone,email) -> str:
        statment=f"insert into {tablename}(CompanyName,RequestData,Location,JobPosition,Salary,Phone,Email) values(?,?,?,?,?,?,?)"
        self.pointer.execute(statment,(companyname,requestdata,location,jobposition,salary,phone,email))
        self.connection.commit()
        return "done"
    
    def SeeInTable(self,tablename) -> tuple:
        statment=f"select * from {tablename}"
        self.pointer.execute(statment)
        result=self.pointer.fetchall()
        return result

    def TableViewer(self,someresult:tuple) -> None:
        for i in someresult:
            pprint(i)

    def CloseConnection() ->str:
        self.connection.closed()
        return "Connection closed"


    def DropTable(self,name) ->str:
        statment=f"drop table {name}"
        self.pointer.execute(statment)
        return f"Droped table {name}"
