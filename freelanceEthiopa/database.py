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
    
    def SeeAll(self):
        self.pointer.execute("select * from Software")
        self.result=self.pointer.fetchall()
        for i in self.result:
            print(i)

    def CheckInMessage(self,message):
        statement="select message from Software where message=%?"
        self.pointer.execute(statement,(message,))
        self.result=self.pointer.fetchall()
        return self.result


    
    
