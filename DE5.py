# 1. How to select a specific columns for making changes?
# 2. Filter rows on the basis of certain conditions?
# 3. Filter rows by combining multiple conditions?

# Ans.1 Square brackets
# Ans.2 and 3 Boolean conditions  

import pandas as pd

data = {
    "Name": ["Vaidik","Sanskar", "Radhika", "Anmol", "Dev", "Vanshika", "Goransh", "Anurag"],
    "Age": [34,23,45,56,43,39,30,40],
    "Salary": [50000,40000,32000,43000,89000,29000,63000,77000],
    "Performace score": [85,87,78,66,87,69,97,69,]
}

df = pd.DataFrame(data)
# print(df)

# Selecting single column

# # print(df["Name"])
# # Another way of doing the same 
# Name = df["Name"]
# print(Name)

# # Selecting multiple columns

# # print(df[['Name', 'Salary']])
# # Another way of doing the same 
# multi = df[['Name', 'Salary']]
# print(multi)

# Filtering rows based on single condition

# # print(df[df['Salary'] > 50000])
# # Another way of doing the same 
# high_salary = df[df['Salary'] > 50000]
# print(high_salary)

# Filtering rows based on multiple conditions

# print(df[(df['Salary'] > 50000) & (df['Salary'] < 80000)])

# AND : When both the conditions are true(&)
high_salary = df[(df['Performace score'] > 90) & (df['Age'] > 50)]
print(high_salary)

# OR : When one of the condition is true(|)
high_salary = df[(df['Performace score'] > 90) | (df['Age'] > 50)]
print(high_salary)