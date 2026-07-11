# Exploratory Data Analysis

import pandas as pd

employee = {
    "Name": ["Rahul", "Priya", "Aniket", "Rohit", "Simran"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [45000, 60000, 75000, 50000, 68000]
}

df = pd.DataFrame(employee)

# unique()
#rint(df["Department"].unique()) # Which departments exist in the company?

# nunique()
#print(df["Department"].nunique()) # "How many different departments are there?"

# value_counts()
print(df["Department"].value_counts()) # How many employees are in each department?

# automatically sorts by frequency (highest to lowest).

