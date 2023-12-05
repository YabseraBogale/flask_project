from pprint import pprint
from database import Database,StackOfTechnology


test=Database()
msg=test.Verified()
count=0
for i in msg:
    try:
        if(str(i[0]).find("[Verified")!=-1):
            name=str(i[0]).split("__________________")[1].split("[Verified")[0].strip('\n')
            count+=1
        elif(str(i[0]).find("(Verified")!=-1):
            name=str(i[0]).split("__________________")[1].split("[Verified")[0].strip('\n')
            count+=1
        elif(str(i[0]).find("(Verified")!=-1):
            name=str(i[0]).split("______")[1].split("[Verified")[0].strip('\n')
    except IndexError as e:
        name=str(i[0]).split("______")
        print(name)
        break

