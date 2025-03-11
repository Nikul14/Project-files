# how can you concatenate two tuples
tup1=(1,"a",True)
tup2=(4,5,7)
print(tup1+tup2)

# how can you initialize a 5*5 numpy array with only zeroes
import numpy as np
n1=np.zeros((5,5))
print(n1)

#Challenge clean data with pandas
import pandas as pd
Data={
    "customer_id":[101,102,103,105,106],
    "name":["Alice","Bob","Charlie","Alice","Bob"],
    "Age":[25,30,None,22,35],
    "Purchase_Amount":[120.5,80.0,None,60.5,75.4],
    "Date":["2024-02-10", "2024-03-05", "2024-01-15", "2024-02-20", "2024-02-25"],
    "Product":["Laptop", "Phone", "Headphones", "Keyboard", "Mouse"]
}

df=pd.DataFrame(Data)
print(df)
df["Date"]=pd.to_datetime(df["Date"])
#handel missing values
missing_values_age=df["Age"].fillna(df["Age"].median(),inplace=True)
print(missing_values_age)
missing_value_amount=df["Purchase_Amount"].fillna(df["Purchase_Amount"].mean(),inplace=True)
print(missing_value_amount)

#drop duplicates
drop_duplicates=df.drop_duplicates(subset=["customer_id","name"],inplace=True)
print(drop_duplicates)
print(df)
print(df.to_string())

#challenge 2 
data={
    "month":["jan-24","jan-24","feb-24","feb-24","mar-24"],
    "product":["laptop","phone","laptop","phone","laptop"],
    "sales":[12000,23000,34000,45000,23000],
    "quantity_sold":[50,100,40,110,45]
      }
df=pd.DataFrame(data)
print(df)

print(df.rename(columns={'month':'Date'},inplace=True))
#convert month into proper datetime format
df['Date']=pd.to_datetime(df["Date"],format="%b-%y")
print(df)

#find the total sales per month
sales_permonth=df.groupby("Date")["sales"].sum().reset_index()
print(sales_permonth)
#sorting
sorting=df.sort_values(by='sales',ascending=False)
print(sorting)
#plot line chart to show highest sales month wise
import matplotlib.pyplot as plt
plt.plot(sorting["sales"],sorting["Date"])
plt.title("SALES PER MONTH")
plt.show()