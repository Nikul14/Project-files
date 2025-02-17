import pandas as pd

# Create a DataFrame with sample data
data = {
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "Charlie", "David", "David", "Bob"],
    "category": ["Animal", "Plant", "Animal", "Animal", "Plant", "Microbe", "Plant", "Animal", "Microbe", "Animal"],
    "value": [10, 15, 20, 25, 30, 5, 10, 35, 40, 20]
}

df = pd.DataFrame(data)

# Save as CSV file
df.to_csv("taxonomy.csv", index=False)

print("File saved as taxonomy.csv")
print(df)
# Example 1: Count the Number of Entries per Name; group by and then apply agg()
group_by = df.groupby('name').size().reset_index(name='count')
print(group_by)
# Example 2: Sum of 'value' per Name
sum_by = df.groupby('name') ['value'].sum().reset_index()
print(sum_by)

#  Multiple Aggregations (sum, mean, count)
multiple_agg = df.groupby('category') ['value'].agg(['sum','mean','count']).reset_index()
print(multiple_agg)
print(df.describe())


#  Merging and Concatenation similar as sql
# df_details= pd.DataFrame({
#     'name':['Alina','Saleena','Kaleena','Sareena'],
#     'age':[25,45,43,23]})
# merged_df= pd.merge(data,df_details,on='name',how='inner')
# print(merged_df)

# Create another DataFrame with extra details
df_details = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40]
})

# Merge on 'name' column (INNER JOIN by default)
merged_df = pd.merge(df, df_details, on="name", how="inner")

print(merged_df)

# Example 6: Sorting Data by Value
sort_df = df.sort_values(by='value',ascending=False)
print(sort_df)

#  Ranking Entries
# If you want to rank people based on their total value, use:

Ranking_df=df['value'].rank(method="dense",ascending=False)
print(Ranking_df)

# Pivot Tables  like excel:
pivot_df=df.pivot_table(values='value',index='name',columns='category',aggfunc='sum',fill_value=0)
print(pivot_df)
# and Crosstabs for frequency count
crosstab = pd.crosstab(df['name'], df['category'])
print(crosstab)








 


