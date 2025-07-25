import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam'],
    "Age": [12,45,32],
    "City":['Nagpur', 'Khandwa', 'Indore']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv")
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)