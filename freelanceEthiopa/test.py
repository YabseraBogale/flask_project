from pprint import pprint
from database import Database,StackOfTechnology


test=Database()

lst=test.CheckInMessage("node")
print(len(lst))