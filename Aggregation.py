import pandas as pd

data = {
    "Name": ['Arun','Varun','Karun'],
    "Age": [23,54,18],
    "Salary": [10000,20000,30000]
}

df = pd.DataFrame(data)
print("Raw DataFrame")

avg_salary = df['Salary'].mean()
print("\nAverage Salary: ",avg_salary)

Maximum_salary = df["Salary"].max()
print("\nMaximum Salary: ", Maximum_salary)

Minimum_salary = df["Salary"].min()
print("\nMinimum Salary: ", Minimum_salary)

Total_sum = df["Salary"].sum()
print("\nSum: ", Total_sum)

# Standard deviation
Std_deviation = df["Salary"].std()
print("\nStandard Deviation: ", Std_deviation)

TOtal_Count = df["Salary"].count()
print("\nTotal: ", TOtal_Count)