import pandas as pd

df=pd.DataFrame({
    "Name": ["Rahul", "Priya", "Anika"],
    "Age": [25, 28, 31],
    "Salary": [45000, 60000, 75000]
})

#print(df)
#Selecting Columns

print(df["Name"])
print(df[["Name","Age"]])
print(df[["Age","Name"]])
print(df[["Name"]])


# Selecting rows using iloc (slicing)

print(df.iloc[0])               # First row (Series)
print(df.iloc[[0,2]])           # Multiple rows (DataFrame)
print(df.iloc[0,2])             # Single cell
print(df.iloc[1:3,0:2])         # Rows 1-2, Columns 0-1
print(df.iloc[0:2,1:3])         # Rows 0-1, Columns 1-2
print(df.iloc[0:2])             # First two rows, all columns
print(df.iloc[:,0])             # All rows, first column
print(df.iloc[:,[0,2]])         # All rows, columns 0 and 2
print(df.iloc[:,:])             # Entire DataFrame


# Selecting rows using loc (no slicing)

import pandas as pd

data={
    "Name": ["Rahul", "Priya", "Anika"],
    "Age": [25, 28, 31],
    "Salary": [45000, 60000, 75000]
}

df=pd.DataFrame(
    data,
    index=["EMP101", "EMP102", "EMP103"]
)

print(df.loc['EMP103'])
print(df.iloc[2])
print(df.loc[["EMP101","EMP103"]])
print(df.loc["EMP102","Name"])

print(df.loc[
    ["EMP102","EMP103"],
    ["Name","Salary"]
])

print(df.loc[
    ["EMP102","EMP103"],
    ["Name","Age"]
])