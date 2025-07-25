import pandas as pd

data = {
    "Name": ['Arun','Varun','Karun'],
    "Age": [23,54,18],
    "Salary": [10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)

# Performing Descending as ascending=False
# Single Column
# df.sort_values(by="Age", ascending=False, inplace=True)
# print("\nSorted Age in descending.")
# print(df)

# Multiple Column
df.sort_values(by=["Age","Salary"], ascending=[False,True], inplace=True)
print("\nSorted Age and Salary.")
print(df)