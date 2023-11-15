import pandas as pd

import json

df=open('freelance_ethio_messages.json')

df=json.load(df)

print(len(df["messages"]))
