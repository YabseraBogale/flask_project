from database import Software
from random import randint
from pprint import pprint
test=Software()




lst=test.SeeInMessage("Verified")
Compaines={}
for i in range(0,100):
    name=lst[i].split("__________________")[1].split("[Verified")[0].strip().upper()
    if name not in Compaines:
        Compaines[name]=1
    else:
        Compaines[name]+=1
    
k=0

for name,count in Compaines.items():
    print(test.InsertCompaines(name,count))