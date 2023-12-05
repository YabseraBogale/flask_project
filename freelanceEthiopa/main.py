from pprint import pprint
from database import Database,StackOfTechnology

def StackOfCompanyUpDate(msg,CompanyStack,ListOfStack):
    Company=CompanyStack.copy()
    for i in ListOfStack:
        if(msg.count(i)!=0 and i not in Company):
            Company[i]=1
        elif(msg.count(i)!=0 and i in Company):
            Company[i]+=1
    return Company

def StackOfCompany(lst,msg):
    Company={}
    for i in lst:
        if(msg.count(i)!=0 and i not in Company):
            Company[i]=msg.count(i)
        elif(msg.count(i)!=0 and i in Company):
            Company[i]+=msg.count(i)
    return Company


def ListSearch(lst):
    name=''
    for i in lst:
        if i.find("Company:")!=-1:
            name=i.replace("(","").replace("[","").split("Company:")[1].rstrip().lstrip()
            if(name==''):
                break
            break
    return name


Data={}
test=Database()
stack=StackOfTechnology().GetAllName()
msg=test.GetAllSoftware()

for i in msg:
    try:
        if(str(i[1]).find("[Verified")!=-1):
            name=str(i[1]).split("__________________")[1].split("[Verified")[0].strip('\n')
            print("from 1",name)
        elif(str(i[1]).find("(Verified")!=-1):
            name=str(i[1]).split("__________________")[1].split("[Verified")[0].strip('\n')
            print("from 2",name)
        elif(str(i[1]).find("(Verified")!=-1):
            name=str(i[1]).split("______")[1].split("[Verified")[0].strip('\n')
            print("from 3",name)
    except IndexError as e:
        name=ListSearch(sorted(list(i[1].split("Verified")[0].split("\n"))))
        print("from 4",name)