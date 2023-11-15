import pandas as pd

import json

df=pd.read_csv('msgs_dataset.csv')

print(df["message"].head())
