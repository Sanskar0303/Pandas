# Removing columns
# Removing column that are of no use keeps your data clean and focused

import pandas as pd

data = {
    "Name": ["Vaidik","Sanskar", "Radhika", "Anmol", "Dev", "Vanshika", "Goransh", "Anurag"],
    "Age": [34,23,45,56,43,39,30,40],
    "Salary": [50000,40000,32000,43000,89000,29000,63000,77000],
    "Performance_score": [85,87,78,66,87,69,97,69]
}

df = pd.DataFrame(data)
print(df)

# Removing a single column
# df.drop(columns = ["Performance_score"], inplace = True)
# print("\nModified data")
# print(df)

# Removing multiple column
df.drop(columns = ["Performance_score", "Age"], inplace = True)
print("\nModified data")
print(df)