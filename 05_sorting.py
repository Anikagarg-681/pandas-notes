import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Ankit", "Rohit", "Simran"],
    "Department": ["HR", "IT", "Finance", "Sales", "IT"],
    "Salary": [45000, 60000, 75000, 50000, 68000]
}

df = pd.DataFrame(employee)

# print(df)

# in ascending order (by default)
#print(df.sort_values(by="Salary"))

# in descending order 
#print(df.sort_values(by="Salary", ascending=False))

# sorting by multiple columns
print(df.sort_values(
    by=["Department", "Salary"]
))
