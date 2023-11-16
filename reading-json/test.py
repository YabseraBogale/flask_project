from database import Software

test=Software()

print(test.createTable())
test.insertIntoTable(2,'hello','2012-12-12')
print(test.seeAll())
