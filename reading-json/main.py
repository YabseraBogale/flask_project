import pandas as pd
from time import sleep
from pprint import pprint
from database import Software
import json
import os


list_of_stack=["mysql","go","python","c++","javascript",
				"js","sql","nodejs","react","vue","php",
				"c#",".net","django","flask","reactjs",
				"larvel","postgres","dart","flutter",
				"durple","java","spring","spring boot",
				"boot","css","bootstrap","tailwind","html"
				"html5","saas","node"]

list_of_job=["backend","frontend","fullstack","full stack",
			"bot","agile","wordpress","git","github","version control",
			"mobile","andriod","ios","iphone","application","stack",
			"data science","ai","machine learning","web","developer",
			"api","rest","mern","lamp","mean","cs","front end"]
df=pd.read_csv('msgs_dataset.csv',low_memory=False)
count=0
table=Software()
Compaine={}


for i in range(0,len(df["message"])):
    try:
        if str(df["message"][i]).find("[Verified")!=-1:
            if(str(df["message"][i]).find("______")!=-1):
                name=str(df["message"][i]).split("______")[1].split("[Verified")[0].strip()
            else:
                name=str(df["message"][i]).split("__________________")[1].split("[Verified")[0].strip()
            if name not in Compaine:
                Compaine[name]=1
                count+=1
            else:
                Compaine[name]=1
                count+=1
        if count==100:
            print("At index",i)
            count=0
            sleep(3)
    except Exception:
        print(i)
        print(df["message"][i])

os.system("clear")
print("Inserting to Database")
count=0
for Name,Request in Compaine.items():
    table.InsertCompaines(Name,Request)
    if count==100:
        print("At index",list(Compaine.keys()).index(Name))
        count=0
        sleep(3)
    else:
        count+=1
