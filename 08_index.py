import pandas as pd

employee = {
    "Employee ID": ["EMP101", "EMP102", "EMP103"],
    "Name": ["Rahul", "Priya", "Anika"],
    "Salary": [45000, 60000, 75000]
}

df = pd.DataFrame(employee)

#print(df)

# set_index()
#print(df.set_index("Employee ID"))

#print(df.index)

# reset_index()
df = df.set_index("Employee ID")
#print(df)
print(df.reset_index())
print(df)
df.reset_index(drop=True)
print(df)
