from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep
count=0
test=Database()
lst=test.SeeAllCompanyTitle()
for i in lst:
    print(type(i))
    if count==5:
        break
    count+=1

print("Count of all Comapny with Job title",len(lst))