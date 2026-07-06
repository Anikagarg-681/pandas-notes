import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Bob", "Rohit", "Simran"],
    "Department": ["HR", "IT", "Finance", "Sales", "IT"],
    "Salary": [45000, 60000, 75000, 50000, 68000]
}

df = pd.DataFrame(employee)
print(df)
print(df["Salary"])

# Which employees earn more than ₹60,000?
print(df["Salary"]>60000) #Boolean Mask.
print(df[df["Salary"]>60000])

# Employees from the IT department.
print(df[df["Department"]=="IT"])

# Department = IT and Salary > 60000

print(
    df[
        (df["Department"]=="IT") &
        (df["Salary"]>60000)
    ]
)


# Show employees from HR OR Finance.

print(
    df[
        (df["Department"]=="HR") |
        (df["Department"]=="Finance")
    ]
)


