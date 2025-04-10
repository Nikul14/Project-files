import pandas as pd
data=pd.read_csv(r"C:\Users\KGE\OneDrive\Desktop\sales_data.csv")
print(data)
print(data.info())
data.isnull().sum()
print(data.describe())
print(data.head(5))
print(data.columns)
#fix date
data["Sale_Date"]=pd.to_datetime(data["Sale_Date"],dayfirst=True,errors="coerce")
print(data.head(5))

# fill
data["Sales_Rep"].fillna("unknown",inplace=True)
data.dropna(subset=["Sale_Date"],inplace=True)
data["Quantity_Sold"]=data["Quantity_Sold"].astype(int)
print(data.head(5))

# EDA
# What are the total sales over time?
import matplotlib.pyplot as plt

# Total sales by date (unsorted to preserve timeline)
total_sale = data.groupby("Sale_Date")["Sales_Amount"].sum().reset_index()

# Plot
plt.figure(figsize=(10, 5))
plt.plot(total_sale["Sale_Date"], total_sale["Sales_Amount"], marker='o', color='teal')
plt.title("Total Sales Over Time")
plt.xlabel("Sale Date")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()


#Which products or regions perform best?
best_region=data.groupby(["Region","Product_ID"])["Sales_Amount"].sum().sort_values(ascending=False).reset_index()
print(best_region)

#Who are the top sales reps?
top_sales_reps=data.groupby("Sales_Rep")["Sales_Amount"].sum().sort_values(ascending=False).reset_index().head(5)
print(top_sales_reps)

# Monthly sales trend
data["Month"]=data["Sale_Date"].dt.to_period('M')
import matplotlib.pyplot as plt

# Create Month column if not already
data["Month"] = data["Sale_Date"].dt.to_period("M")

# Group by Month and sum sales
monthly_sales = data.groupby("Month")["Sales_Amount"].sum().reset_index()

# Convert Period to datetime for plotting
monthly_sales["Month"] = monthly_sales["Month"].astype(str)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month"], monthly_sales["Sales_Amount"], marker='o', linestyle='-', color='darkblue')
plt.title("Monthly Sales Trend", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales Amount", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()





