from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep

test=Database()
lst=test.SeeAllCompanyTitle()
for i in lst:
    pprint(i[1])