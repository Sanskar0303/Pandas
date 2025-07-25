# Updating all the values exist in the column

import pandas as pd

data = {
    "Name": ["Vaidik","Sanskar", "Radhika", "Anmol", "Dev", "Vanshika", "Goransh", "Anurag"],
    "Age": [34,23,45,56,43,39,30,40],
    "Salary": [50000,40000,32000,43000,89000,29000,63000,77000],
    "Performace_score": [85,87,78,66,87,69,97,69]
}

df = pd.DataFrame(data)
print(df)

# increasing all the salary by 5%
df["Salary"] = df["Salary"] * 1.05
print(df)