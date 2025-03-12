import pandas as pd
Data={
    "customers_id":	[101,102,101,103,104,105,102,103],
    "customer_name":["Alice","Bob",'Charlie',"Alice","David","Eva","Bob","Charlie"],
    "Purchase_Amount":[500,700,'Nan',1000,250,900,1500,600]	,
    "Purchase_Date":["2024-03-01","2024-03-02","2024-03-05","2024-03-06","2024-03-08","2024-03-10","2024-03-12","2024-03-15"]
}
df=pd.DataFrame(Data)
print(df)
print(df.isnull().sum())

#1.Handle Missing values

df["Purchase_Amount"]=pd.to_numeric(df["Purchase_Amount"],errors='coerce')
df["Purchase_Amount"].fillna(df["Purchase_Amount"].median(),inplace=True)
print(df["Purchase_Amount"])

#2.TOP 5 customers who spent the most

top_customrs=df.groupby('customer_name')["Purchase_Amount"].sum().reset_index()
top_customrs=top_customrs.sort_values(by="Purchase_Amount",ascending=False).head(5)
print(top_customrs)

#3.Calculate the avg.purchase amount per customer
avg_custmers_peramount=df.groupby("customer_name")["Purchase_Amount"].mean().reset_index()
print(avg_custmers_peramount)

#4. Repeated customers who purchase more than 1
repeated_customers=df["customer_id"].value_counts()
repeated_customers=repeated_customers[repeated_customers>1]
print(repeated_customers)

