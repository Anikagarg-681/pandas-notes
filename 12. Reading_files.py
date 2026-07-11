# Read the CSV

import pandas as pd

df = pd.read_csv("employees.csv")


# Writing a CSV
df.to_csv("cleaned_data.csv", index=False)

# Reading Excel Files
df = pd.read_excel("employees.xlsx")


# concat()
pd.concat([df1, df2]) # used two merge two df

# merge()
pd.merge(df1, df2, on="ID") # pd.merge(df1, df2, on="ID")

# groupby()
df.groupby("Department")["Salary"].mean()  # What's the average salary in each department?
