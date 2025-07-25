import pandas as pd

data = {
    "Name": ['Arun','Varun','Karun','Narun','Karun'],
    "Age": [24,24,22,43,22],
    "Salary": [50000,60000,45000,52000,35000]
}

df = pd.DataFrame(data)

# Single columns
# grouped = df.groupby("Age")["Salary"].sum()
# print(grouped)

# Multiple columns
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)