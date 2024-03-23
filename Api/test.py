import sqlite3
from search import Search


searcher=Search()

connection=sqlite3.Connection("freelance-data-v2.db")

pointer=connection.cursor()

pointer.execute("select nameOfCompany from Company")

result=pointer.fetchall()

for i in result:
    companyname=i[0]
    print(type(companyname))