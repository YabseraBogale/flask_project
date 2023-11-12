"""
 Name: Vaccum cleaner
 Author: Yabsera Bogale
"""
from random import randint



lst=[]


for i in range(1,10):
	if(randint(1,100)%i==0):
		lst.append("dirty")
	else:
		lst.append("cleand")

agent_action=[]

for i in lst:
	if i=="cleand":
		agent_action.append("passed")
	else:
		agent_action.append("dirty to cleanned")


print("room before",lst)
print("room after",agent_action)

