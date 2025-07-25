# After identifying the missing values.
# Understanding how to handle data via
# 1.dropna() for removing 
# 2.fillna() for filling 

import pandas as pd

data = {
    "Name": ["Vaidik", None, "Radhika", "Anmol", "Dev", "Vanshika", "Goransh", "Anurag"],
    "Age": [34, None,45,56,43,39,30,40],
    "Salary": [50000,None,32000,43000,89000,29000,63000,77000],
    "Performance_score": [85,None,78,66,87,69,97,69]
}

df = pd.DataFrame(data)
print(df)

# Understanding Removing Data.
# df.dropna(inplace = True)
# print("Removing Rows.")
# print(df)

# df.dropna(axis = 1, inplace = True)
# print("Removing Columns.")
# print(df)

# Understanding Filling Data.
# filling 0zero
# df.fillna(0, inplace = True)
# print("\nFilling  Rows.")
# print(df)

# filling mean value which is for Numeric values

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_score'].fillna(df['Performance_score'].mean(), inplace=True)

# filling mean value which is for Alphabetical values

df['Name'].fillna(df['Name'].mode()[0], inplace=True)
print(df)