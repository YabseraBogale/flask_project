from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep

test=Database().GetAllSoftware()[0:10]

for i in test:
    print(i)


