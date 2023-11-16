import pandas as pd

import json

list_of_stack=["mysql","go","python","c++","javascript",
				"js","sql","nodejs","react","vue","php",
				"c#",".net","django","flask","reactjs",
				"larvel","postgres","dart","flutter",
				"durple","java","spring","spring boot",
				"boot","css","bootstrap","tailwind","html"
				"html5","saas","node"]

df=pd.read_csv('msgs_dataset.csv')
count=0
for i in range(0,100):
	print(df["message"][i])
