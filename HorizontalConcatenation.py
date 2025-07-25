import pandas as pd

df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [23, 34]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Age": [28, 40]
})

# Concatenate (row-wise)
result = pd.concat([df1, df2], axis=1)
print(result)