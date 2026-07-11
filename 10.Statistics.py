import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Aniket", "Rohit", "Simran"],
    "Age": [25, 28, 31, 27, 29],
    "Salary": [45000, 60000, 75000, 50000, 68000]
}

df = pd.DataFrame(employee)

#print(df)

# describe()
#print(df.describe())

# count- How many non-missing values
# std- How spread out are the values

# mean()
#print(df["Salary"].mean())

# max()
#print(df["Salary"].max())

# min()
#print(df["Salary"].min())

# count()
#print(df["Salary"].count())

# median()
#print(df["Salary"].median())

# mode()
print(df["Salary"].mode())  # Most frequent value
