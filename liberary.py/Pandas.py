# # import pandas as pd

# # Load CSV file
# import pandas as pd

# Load the Titanic CSV file
# file_path = "/mnt/data/titanic.csv"
# df = pd.read_csv(file_path)

# # # Display the first 5 rows
# # print(df.head())
# # pd.read_csv("c:\Users\KGE\Downloads\titanic.csv")
import pandas as pd
# #define ,analysing with 'df' function
df = pd.read_csv(r"C:\Users\KGE\Downloads\titanic.csv")  # Add 'r' before the path
print(df)
# df.head() #to view starting data 
# df.tail() #to view end data
# df
# df.dtypes
# print(df.dtypes)
# print(df.describe())
# column = df[['Name','Sex','Ticket','Cabin','Embarked']]
# print(column)
# index = df[df.dtypes[df.dtypes=='float'].index]
# print(index)
# print(df.columns)
# sex = df[['Sex']] # to see specific column
# print(sex)
# slicing = df[['Sex']] [4:15:]#slicing to lookup from 4 to 14
# print(slicing)
# new_column = df['New col']=0
# print(new_column)
# print(df)

# new_location = df.insert(loc=3,column='food',value='lunch')
# print(new_location)
# print(df)

# #create with pd.series 

# a = df['Name'] [0:10]
# print(a)
# l= ['a','b','c','d','f','g','h','i','j','k']
# n= pd.Series(list(a),index=l)
# print(n)

# m1=pd.Series([100,200,300,400],index=[1,2,3,4])
# print(m1)

# m2=pd.Series([500,600,700,800],index=[5,6,7,8])
# print(m2)

# m3 = pd.concat([m1,m2])
# print(m3)

# #access via indexing
# print(m1[1])
# #multiply
# # Multiplying by a scalar
# # df_mul_scalar = df * 2  # Multiplies all elements by 2

# # Multiplying another DataFrame (element-wise)
# # import pandas as pd

# # # Creating a DataFrame
# # df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# # # Adding a scalar (number)
# # df_add_scalar = df + 10  # Adds 10 to all elements

# # # Adding another DataFrame (element-wise)
# # df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
# # df_add_df = df + df2  # Adds corresponding elements

# # print(df_add_scalar)
# # print(df_add_df)

# # # Multiplying by a scalar
# # df_mul_scalar = df * 2  # Multiplies all elements by 2

# # # Multiplying another DataFrame (element-wise)
# # df_mul_df = df * df2  # Multiplies corresponding elements

# # print(df_mul_scalar)
# # print(df_mul_df)

# # delete column
# # col_del=df.drop('Sex',axis=1)

# # print(df.columns)

# # df.drop('food',axis=1,inplace=True)

# # print(df)
# # print(df.columns)

# #14feb see u 
# # top_rows = df.head()
# # print(top_rows)
# # print(df.drop(3))
# # print(df)
# # permanent_drop = df.drop(3,inplace=True)
# # print(permanent_drop)
# # print(df)

# # add_column = df.insert(loc=3,column='Economy',value='NAN')
# # print(add_column)
# # print(df) 
 #add rows using loc()
new_row = df.loc(1)
print(new_row)

# print(df.set_index('Name',inplace=True)) #to set index permanently
# print(df)
print(df.reset_index())
# print(df)
#data frame via dictionary
dict_pd = {'Name':['A','B','C','D','E'],'Class':[1,2,3,4,5],'Grade':['EX','VG','VB','AVG','POOR']}
# print(dict_pd)
d=pd.DataFrame(dict_pd)
print(d)

print(df)




 


 


