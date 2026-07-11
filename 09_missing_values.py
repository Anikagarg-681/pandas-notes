# Creating a DataFrame with Missing Values
import pandas as pd
import numpy as np

employee = {
    "Name": ["Rahul", "Priya", "Ankit", "Rohit"],
    "Age": [25, 28, np.nan, 27],
    "Salary": [45000, 60000, 75000, np.nan]   # np.nan means value is missing
}

df = pd.DataFrame(employee)

print(df)

# Finding missing values 
print(df.isnull())

# Counting Missing Values
print(df.isnull().sum())

import pandas as pd
import numpy as np

employee = {
    "Name": ["Rahul", "Priya", "Aniket", "Rohit"],
    "Age": [25, 28, np.nan, 27],
    "Salary": [45000, 60000, 75000, np.nan]
}

df = pd.DataFrame(employee)

print(df)

# dropna() (Delete them)

print(df.dropna()) # By default, Pandas deletes the entire row if any value in that row is missing.

print(df.dropna(how="all")) # Delete rows only if every value is missing.


# Filling values
print(df.fillna(30))  # Replace every missing value in the entire DataFrame with 30.

# Filling Only One Column
df["Age"] = df["Age"].fillna(30)
print(df)

# Filling Different Columns with Different Values
df=df.fillna({
    "Age":30,
    "Salary":65000
})
print(df)

import pandas as pd
import numpy as np

employee = {
    "Name": ["Rahul", "Priya", "Aniket", "Rohit"],
    "Age": [25, 28, np.nan, 27],
    "Salary": [45000, 60000, 75000, np.nan]
}

df = pd.DataFrame(employee)
print(df)
# Fill it with the average age.
 
df["Age"] = df["Age"].fillna(df["Age"].mean()) # Mean 
print(df)

df["Salary"] = df["Salary"].fillna(df["Salary"].median()) # Median
print(df)

# Mean → when data is fairly symmetric.
# Median → when there are extreme outliers.

df["Department"] = df["Department"].fillna("Unknown")