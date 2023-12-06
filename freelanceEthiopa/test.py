from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep

test=Database()
phone=test.CheckInMessageSoftware("Phone")
location=test.CheckInMessageSoftware("location")
phoneandlocation=test.GetLocationAndPhoneFromSoftWare()

print("Number of phone number",len(phone))
print("Number of location",len(location))
print("Both together",len(phoneandlocation))