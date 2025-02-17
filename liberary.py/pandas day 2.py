# DATA CLEANING FUNCTIONS
#  When to Use inplace=True?
# ✅ When working with large datasets to save memory
# ✅ When you don't need the original DataFrame anymore


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/sonwaneshivani/Data-Science-Learning/refs/heads/main/taxonomy.csv")
print(df)


# TO REMOVE MISSING DATA in a ROWS
# print(df.dropna(inplace=True)) # always add inplace for permanent change
# print(df)

# TO REMOVE MISSING DATA FROM A COLUMN
# print(df.dropna(axis=1,inplace=True))
# print(df)

print(df)
#now i have to fill NAN with another paramenter
print(df.fillna('str',inplace=True))
print(df)
#group by:
group_by = df.groupby('name').size().reset_index(name='count')
print(group_by)










