# Understanding Head() and Tail()

import pandas as pd
df = pd.read_json("sample_Data.json")

print("Display 10 rows of first.")
print(df.head(10))      #head()

print("Display 10 rows of last.")
print(df.tail(10))      #tail()