from pprint import pprint
from database import Database,StackOfTechnology
from time import sleep



def ListSearch(lst):
    name=''
    for i in lst:
        if i.find("Company:")!=-1:
            name=i.replace("(","").replace("[","").split("Company:")[1].rstrip().lstrip()
            if(name==''):
                break
            break
    return name

def StackOfCompanyUpDate(msg,CompanyStack,ListOfStack):
    Company=CompanyStack.copy()
    for i in ListOfStack:
        if(msg.count(i)!=0 and i not in Company):
            Company[i]=msg.count(i)
        elif(msg.count(i)!=0 and i in Company):
            Company[i]+=msg.count(i)
    return Company
    
def StackOfCompany(lst,msg):
    Company={}
    for i in lst:
        if(msg.count(i)!=0 and i not in Company):
            Company[i]=msg.count(i)
        elif(msg.count(i)!=0 and i in Company):
            Company[i]+=msg.count(i)
    return Company

Data={}
test=Database()
stack=StackOfTechnology().GetAllName()
msg=test.GetAllSoftware()
for i in msg:
    try:
        if(str(i[1]).find("[Verified")!=-1):
            name=str(i[1]).split("__________________")[1].split("[Verified")[0].strip('\n')
            if name not in Data:
                Data[name]={"Request":1,"stack":StackOfCompany(stack,i[1])}
            else:
                Data[name]["Request"]+=1
        elif(str(i[1]).find("(Verified")!=-1):
            name=str(i[1]).split("__________________")[1].split("[Verified")[0].strip('\n')
            if name not in Data:
                Data[name]=1
            else:
                Data[name]+=1
            
        elif(str(i[1]).find("(Verified")!=-1):
            name=str(i[1]).split("______")[1].split("[Verified")[0].strip('\n')
            if name not in Data:
                Data[name]=1
            else:
                Data[name]+=1
            
    except IndexError as e:
        name=ListSearch(sorted(list(i[1].split("Verified")[0].split("\n"))))
        if name not in Data:
            Data[name]=1
        else:
            Data[name]+=1

pprint(Data)  

        

