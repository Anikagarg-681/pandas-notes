import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Ankit", "Rohit", "Simran"],
    "Department": ["HR", "IT", "Finance", "Sales", "IT"],
    "Salary": [45000, 60000, 75000, 50000, 68000]
}

df = pd.DataFrame(employee)

print(df)

# Creating a column
df["Bonus"]=[1000,2000,5000,3000,4000]
print(df)

# if bonus column already exists then it will overwrite the values
df["Bonus"] = [1000, 1000, 1000, 1000, 1000]
print(df)
 
# Creating a Column from Existing Columns
df["Total Income"]= df["Salary"]+ df["Bonus"] #vectorized operations Pandas automatically performs the operation for every row.
print(df)

# Modifying an Existing Column
df["Salary"]=df["Salary"]+5000
print(df)

# Modifying Only One Cell
df.loc[2,"Salary"]= 80000 # using loc 
print(df)

df.iloc[2, 2] = 80000 #using iloc
print(df)
