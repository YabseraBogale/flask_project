from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep
count=0
test=Database()
lst=test.SeeAllCompanyTitle()
for i in lst:
    pprint(i)
    if count==5:
        break
    count+=1