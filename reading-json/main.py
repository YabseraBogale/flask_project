import pandas as pd

import json

df=open('msgs_dataset.csv')

df=json.load(df)

print(len(df["messages"]))
