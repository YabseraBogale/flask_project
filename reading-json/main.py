import pandas as pd

import json

list_of_stack=["mysql","go","python","c++","javascript","js","sql","nodejs","react","vue",""]

df=pd.read_csv('msgs_dataset.csv')

for i in range(0,100):
	print(type(df["message"][i]))
