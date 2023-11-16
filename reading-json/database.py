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
		
	def count(self):
		self.pointer.execute("select count(*) from Software")
		self.result=self.pointer.fetchone()
		return self.result
	
	def close(self):
		self.cursor.close()
		return "closed"	
	
