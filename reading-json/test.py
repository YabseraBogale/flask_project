from database import Software
from random import randint
test=Software()

lst=test.SeeInMessage("Verified")

for i in range(0,100):
    print(lst[i].split("__________________")[1].split("[Verified")[0].strip())
    
