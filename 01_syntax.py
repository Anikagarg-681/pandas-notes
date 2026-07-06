#Creating Series 

import pandas as pd

ages=pd.Series([21,24,27,30])
print(ages)
print(type(ages))


# Creating Series with Custom Index

import pandas as pd

marks=pd.Series([86,54,98], index=["Bob","Ronny","Daniel"])
print(marks)
print("Marks of Ronny:", marks["Ronny"])


# Creating Series Using Dictionary

import pandas as pd

marks=pd.Series({"Bob":77, "Ronny":89, "Daniel":53})
print(marks)


# Creating Data Frame 

import pandas as pd

df=pd.DataFrame({
    "Name":["Nick","Sam","Joe"],
    "Age":[43,39,35],
    "Salary":[30000,69000,50000]

})
print(df)

