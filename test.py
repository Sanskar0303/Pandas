import pandas as pd

# #read data from CSV file into a dataframe
# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# #read data from XLSX (excel) file into a dataframe
# df = pd.read_excel("SampleSuperstore.xlsx")

#read data from JSON file into a dataframe
df = pd.read_json("sample_Data.json")

print(df)