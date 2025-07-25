# Understanding info()

# import pandas as pd

# df = pd.read_json("sample_Data.json")

# print("Displaying the info of dataset.")
# print(df.info())

# For example: Lets take a small data set
import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam'],
    "Age": [12,45,32],
    "City":['Nagpur', 'Khandwa', 'Indore']
}

df = pd.DataFrame(data)

print("Displaying the info of dataset.")
print(df.info())