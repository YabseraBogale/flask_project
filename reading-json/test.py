from database import Software

test=Software()
path='freelance-data.db'
print(test.ConnectToDatabase(path))
#print(test.createTable())
