import sqlite3

class StackOfTechnology():
    
    def __init__(self):
        self.list_of_stack=["mysql","go","python","c++","javascript",
	        			"js","sql","nodejs","react","vue","php",
		        		"c#",".net","django","flask","reactjs",
			         	"larvel","postgres","dart","flutter",
				        "durple","java","spring","spring boot",
				        "boot","css","bootstrap","tailwind","html"
				        "html5","saas","node","backend","frontend","fullstack","full stack",
	    	    	    "bot","agile","wordpress","git","github","version control",
		    	        "mobile","andriod","ios","iphone","application","stack",
			            "data science","ai","machine learning","web","developer",
			            "api","rest","mern","lamp","mean","cs","front end"
                    ]
    
    def GetAllName(self):
        return self.list_of_stack

class Database():

    def __init__(self):
        self.cursor=sqlite3.Connection("./freelance-data.db")
        self.pointer=self.cursor.cursor()
    
    def SeeAllSoftware(self):
        self.pointer.execute("select * from Software")
        self.result=self.pointer.fetchall()
        for i in self.result:
            print(i)
    
    def GetAllSoftware(self):
        self.pointer.execute("select * from Software")
        self.result=self.pointer.fetchall()
        return self.result

    def InsertIntoCompanyTable(self,id,nameOfCompany,numberOfRequest,listOfStack):
        statment="insert into Company(id,nameOfCompany,numberOfRequest,listOfStack) values(?,?,?,?)"
        self.pointer.execute(statment,(id,nameOfCompany,numberOfRequest,str(listOfStack)))
        self.cursor.commit()
        return "done"

    def MakeData(self):
        statment="""
                create table Company(
	                id int not null primary key,
	                nameOfCompany varchar(30) not null,
	                numberOfRequest int not null,
	                listOfStack text not null
                );
                """
        self.pointer.execute(statment)
        self.cursor.commit()

    def DropTableSoftware(self):
        sure=input("Are you sure you want to delete the data ? 'Y' for yes or 'N' for no ? ")
        if sure=='Y':
            statement="drop table Software"
            self.pointer.execute(statement)
            self.cursor.commit()
            return "done"
        return "Not deleted"
    def DropTableCompany(self):
        sure=input("Are you sure you want to delete the data ? 'Y' for yes or 'N' for no ? ")
        if sure=='Y':
            statement="drop table Company"
            self.pointer.execute(statement)
            self.cursor.commit()
            return "done"
        return "Not deleted"

    def DeleteTableSoftwareWithId(self,id):
        sure=input("Are you sure you want to delete the data ? 'Y' for yes or 'N' for no ? ")
        if sure=='Y':
            statement="delete from Software where id=?"
            self.pointer.execute(statement,(id,))
            self.cursor.commit()
            return "done"
        return "Not deleted"
    
    def DeleteTableCompanyWithId(self,id):
        sure=input("Are you sure you want to delete the data ? 'Y' for yes or 'N' for no ? ")
        if sure=='Y':
            statement="delete from Company where id=?"
            self.pointer.execute(statement,(id,))
            self.cursor.commit()
            return "done"
        return "Not deleted"

    def GiveMeAllCompanyName(self):
        statement="select nameOfCompany from Company"
        self.pointer.execute(statement)
        self.result=self.pointer.fetchall()
        return self.result

    def CheckInMessageSoftware(self,message):
        statement=f"select message from Software"
        self.pointer.execute(statement)
        self.result=self.pointer.fetchall()
        self.lst=[]
        for i in self.result:
            if(str(i[0]).find(message)!=-1):
                self.lst.append(i[0])
        return self.lst

    def GetLocationOrPhoneFromSoftWare(self):
        statement=f"select message from Software"
        self.pointer.execute(statement)
        self.result=self.pointer.fetchall()
        self.lst=[]
        for i in self.result:
            if(str(i[0]).find("location")!=-1 or str(i[0]).find("phone")!=-1):
                self.lst.append(i[0])
            elif(str(i[0]).find("Location")!=-1 or str(i[0]).find("Phone")!=-1):
                self.lst.append(i[0])
            elif(str(i[0]).find("Location")!=-1 or str(i[0]).find("phone")!=-1):
                self.lst.append(i[0])
            elif(str(i[0]).find("location")!=-1 or str(i[0]).find("Phone")!=-1):
                self.lst.append(i[0])
        return self.lst

    
    def GetLocationAndPhoneFromSoftWare(self):
        statement=f"select message from Software"
        self.pointer.execute(statement)
        self.result=self.pointer.fetchall()
        self.lst=[]
        for i in self.result:
            if(str(i[0]).find("location")!=-1 and str(i[0]).find("phone")!=-1):
                self.lst.append(i[0])
            elif(str(i[0]).find("Location")!=-1 and str(i[0]).find("Phone")!=-1):
                self.lst.append(i[0])
        return self.lst
    
    
    
    
