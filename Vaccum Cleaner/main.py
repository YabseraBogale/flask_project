"""
 Name: Vaccum cleaner
 Author: Yabsera Bogale
 github: YabseraBogale

"""
from pprint import pprint
print("Enter \"f\" to Finish")
q='go'
lst=[]
while q!="f":
	q=input("Enter \"d\" for dirty or \"c\" for clean: ")
	if q=="d":
		lst.append([q,"cleaned"])
	elif q=="c":
		lst.append([q,"passed"])
	else:
		print("Enter the right format")
		
print("Finished")
print("Room Histroy")
pprint(lst)





