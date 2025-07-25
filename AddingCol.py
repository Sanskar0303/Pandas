# Adding new column

import pandas as pd

data = {
    "Name": ["Vaidik","Sanskar", "Radhika", "Anmol", "Dev", "Vanshika", "Goransh", "Anurag"],
    "Age": [34,23,45,56,43,39,30,40],
    "Salary": [50000,40000,32000,43000,89000,29000,63000,77000],
    "Performace_score": [85,87,78,66,87,69,97,69]
}

df = pd.DataFrame(data)
print("\nDefault dataset")
print(df)

# Adding column: Assignment(This will always add the column at the end)
df['Bonus'] = df['Salary'] * 0.10
print("\nAdding Bonus column at last")
print(df)

# Adding column at a specific location: insert()
df.insert(0, "Employee_ID", [10,20,30,40,50,60,70,80])
print("\nAdding column Employee_ID at specific location")
print(df)