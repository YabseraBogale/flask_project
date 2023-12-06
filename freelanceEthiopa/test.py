from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep

test=Database()
phone=test.CheckInMessageSoftware("Phone")


pprint(len(phone))

