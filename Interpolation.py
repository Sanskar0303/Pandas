# # Undertanding concept of Interpolation.
# # interpolate()

# import pandas as pd

# data = {
#     "Name": ["Vaidik", "Ram", "Radhika", "Anmol", "Dev", "Vanshika", "Goransh", "Anurag"],
#     "Age": [34,None,45,56,43,39,30,40],
#     "Salary": [50000,None,32000,43000,89000,29000,63000,77000],
#     "Performance_score": [85,None,78,66,87,69,97,69]
# }

# df = pd.DataFrame(data)
# print(df)

# df.interpolate(method = "linear")