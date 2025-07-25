import pandas as pd

# customer DataFrame
df_customers = pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["Ramesh","Suresh","Kalpesh"]
})

# order DataFrame
df_orders = pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250,400,350]
})

# Merge
df_merge = pd.merge(df_customers, df_orders, on="CustomerID", how="left ")
print("\nOuter Join.")
print(df_merge)