import pandas as pd
from time import sleep
from database import Software
import json

list_of_stack=["mysql","go","python","c++","javascript",
				"js","sql","nodejs","react","vue","php",
				"c#",".net","django","flask","reactjs",
				"larvel","postgres","dart","flutter",
				"durple","java","spring","spring boot",
				"boot","css","bootstrap","tailwind","html"
				"html5","saas","node"]

df=pd.read_csv('msgs_dataset.csv',low_memory=False)
count=0
table=Software()
for i in range(0,10):
	
	if df["message"][i].find("#Software_design_and_Development")!=-1:
		table.insertIntoTable(i,df["message"][i],df["date"][i])
	
	if count==100:
		count=0
		sleep(3)
	else:
		count+=1

