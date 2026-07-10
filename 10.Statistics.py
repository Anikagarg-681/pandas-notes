import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Anika", "Rohit", "Simran"],
    "Age": [25, 28, 31, 27, 29],
    "Salary": [45000, 60000, 75000, 50000, 68000]
}

df = pd.DataFrame(employee)

print(df)

# describe()
print(df.describe())
