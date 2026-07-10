import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Ankit", "Rohit", "Simran"],
    "Department": ["HR", "IT", "Finance", "Sales", "IT"],
    "Salary": [45000, 60000, 75000, 50000, 68000],
    "Bonus":[5000,1000,5000,1000,2000]
}

df = pd.DataFrame(employee)
print(df)

df["Total Income"]= df["Salary"]+ df["Bonus"]
print(df)

# Deleting a Column
print(df.drop(columns=["Total Income"]))

# Deleting  Multiple Columns
print(df.drop(columns=["Bonus","Total Income"]))

print(df)

# Deleting a Row
print(df.drop(index=0))

# Deleting Multiple Rows
print(df.drop(index=[1,4]))

# Delete Rows After Filtering
print(df.drop(df[df["Salary"] < 50000].index))

# Permanently delete
df = df.drop(columns=["Bonus"])  #method-01
print(df)

df.drop(columns=["Bonus"], inplace=True)  #method-02
