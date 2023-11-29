# going to rewrite the whole thing in java in the next 5-6 month

import sqlite3
from random import randint
from time import sleep


class Software():
	
	def __init__(self):
		self.cursor=sqlite3.Connection('database.db')
		self.pointer=self.cursor.cursor()
	def ConnectToDatabase(self,path):
		self.cursor=sqlite3.Connection(path)
		self.pointer=self.cursor.cursor()
		return "Connected"
	
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
				if count==5:
					return True
		return False
	
	def DropSoftWareTable(self):
		statement="drop table Software"
		self.pointer.execute(statement)
		self.cursor.commit()
		return "Dropped Software Table"
	
	def DropCompainesTable(self):
		statement="drop table AllCompaines"
		self.pointer.execute(statement)
		self.cursor.commit()
		return "Dropped Compaines Table"
	
	def DropErrTable(self):
		statement="drop table Err"
		self.pointer.execute(statement)
		self.cursor.commit()
		return "Dropped Compaines Table"
	
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
		statment="""
				create table IF NOT EXISTS AllCompaines(
					NumberOfRequestMade int not null,
					CompanyName varchar(30) not null	
				);
				"""
		self.pointer.execute(statment)
		self.cursor.commit()
		statment="""
					create table IF NOT EXISTS Err(
						indexOfMessage int not null,
						message text not null
					);
				"""
		self.pointer.execute(statment)
		self.cursor.commit()
		return "Done"
		
	def seeAll(self):
		self.pointer.execute("select * from Software")
		self.result=self.pointer.fetchall()
		return self.result
		
	def checkIfItExists(self,id):
		statment="select * from Software where id=?"
		self.pointer.execute(statment,(id,))
		self.result=self.pointer.fetchone()
		return self.result
	
	def countSotware(self):
		self.pointer.execute("select count(*) from Software")
		self.result=self.pointer.fetchone()
		return self.result

	def countCompaines(self):
		self.pointer.execute("select count(*) from Compaines")
		self.result=self.pointer.fetchone()
		return self.result
	
	def InsertIntoErr(self,Index,Message):
		statment="insert into Err(indexOfMessage,message) values(?,?)"
		self.pointer.execute(statment,(Index,Message))
		self.cursor.commit()

	def InsertCompaines(self,Name,Count):
		statment="insert into AllCompaines(CompanyName, NumberOfRequestMade) values (?,?)"
		self.pointer.execute(statment,(Name,Count))
		self.cursor.commit()
		return "Done"

	def SeeInMessage(self,ToFindMessage):
		statement="select message from software"
		self.pointer.execute(statement)
		self.result=self.pointer.fetchall()
		self.lst=[]
		for i in self.result:
			if i[0].find(ToFindMessage)!=-1:
				self.lst.append(i[0])
		return self.lst
	
	def close(self):
		self.cursor.close()
		return "closed"	
	
