from database import Software

test=Software()
path='./freelance-data.db'
print(test.ConnectToDatabase(path))
#print(test.createTable())
lst=test.SeeInMessage('Verified')

for i in range(0,10):
    print(lst[i])
