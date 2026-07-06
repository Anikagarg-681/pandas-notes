import pandas as pd
df=pd.DataFrame({
    "Name": ["Rahul", "Priya", "Jayant", "Rohit", "Simran", "Aman"],
    "Department": ["HR", "IT", "Finance", "Sales", "IT", "HR"],
    "Salary": [45000, 60000, 75000, 50000, 68000, 47000]
    
})
# Head()
'''
print(df)
print(df.head())
print(df.head(2))
print(df.head(20))
'''
# Tail
'''
print(df.tail())
print(df.tail(2))
'''

# Shape 
'''
print(df.shape)
'''

# Columns
'''
print(df.columns)
print(df.columns[1])
'''

# Data types of columns 
'''
print(df.dtypes)
'''

df.info()