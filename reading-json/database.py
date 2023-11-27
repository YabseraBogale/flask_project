# going to rewrite the whole thing in java in the next 5-6 month

import sqlite3
from time import sleep


class Software():
	
	def __init__(self):
		self.cursor=sqlite3.Connection('database.db')
		self.pointer=self.cursor.cursor()
	
	def insertIntoTable(self,id,message,date):
		statment="insert into Software(id,message,date) values(?,?,?)"
		self.pointer.execute(statment,(id,message,date))
		self.cursor.commit()
		return "Done"
	# check this if there is better method or not 
	def checkAllWith(self,lst,message):
		count=0
		for i in lst:
			if str(message).lower().find(i)!=-1:
				count+=1
				if count==3:
					return True
		return False
		
	def createTable(self):
		statment="""
				create table IF NOT EXISTS Software(
					id int not null primary key,
					message text not null,
					date datetime not null
				);
				"""
		self.pointer.execute(statment)
		self.cursor.commit()
		return "Done"
		
	def seeAll(self):
		self.pointer.execute("select * from Software")
		self.result=self.pointer.fetchall()
		return self.result
		
	def checkIfItExists(id):
		statment="select id from Software where id=?"
		self.pointer.execute(statment,(id,))
		self.result=self.pointer.fetchone()
		return self.result
	
	def count(self):
		self.pointer.execute("select count(*) from Software")
		self.result=self.pointer.fetchone()
		return self.result
	
	def SeeInMessage(self,ToFindMessage):
		statement="select from message from software where message='%?%'"
		self.pointer.execute(statement,(ToFindMessage,))

	def close(self):
		self.cursor.close()
		return "closed"	
	
