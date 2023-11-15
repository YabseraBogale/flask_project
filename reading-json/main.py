import pandas as pd

import json

df=pd.read_csv('msgs_dataset.csv')

for i in range(0,100):
	print(type(df["message"][i]))
