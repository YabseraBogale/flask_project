import sqlite3


class Software():
	self.cursor=sqlite3.Connection('database.py')
	self.pointer=self.connect.cursor()
	
	def insertIntoTable(self,id,message,date):
		statment="insert into Software(id,message,date) values(?,?,?)"
		self.pointer.execute(statment,(id,message,date))
		self.cursor.commit()
		return "Done"
