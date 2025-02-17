

# Load the Data :

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv(r"https://raw.githubusercontent.com/SachinkumarSakthivel/PROJECT-1/refs/heads/main/apple_products.csv")
print(df)
print(df.info()) # it tells all the info.of data all including null values

for idx, (col, dtype) in enumerate(df.dtypes.items()):#data types and their index
    print(f"Index: {idx}, Column: {col}, Data Type: {dtype}")

#DATA CLEAN 

print(df.isnull().sum()) # 1.check is their null value and hai toh kithni data.isnull().sum()
print(df.drop_duplicates(inplace=True))
print(df.fillna(0,inplace=True))

#data discribe Exploratory Data Analysis (EDA):

print(df.describe())
total_sales = df["Sale Price"].sum()
print("Total Sales:", total_sales)
                            
#Sales Performance Analysis:

highest_rated=df.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated["Product Name"])

#LETS HAVE A LOOK AT THE NUMBER OF RATING OF THE HIGHEST RATES IPHONE ON FLIPKART

iphone=highest_rated["Product Name"].value_counts()
print(iphone)
labels=iphone.index
print(labels)
counts=highest_rated["Number Of Ratings"]
print(counts)

# : Visualization

# fig=px.bar(highest_rated,x=labels,y=counts,title="Number of Rating of highest rated i phones")
# fig.show()


import plotly.express as px

# Ensure correct column names and sorting
highest_rated = highest_rated.sort_values(by="Number Of Ratings", ascending=False)

# Creating an improved bar chart
fig = px.bar(
    highest_rated, 
    x="Product Name",  
    y="Number Of Ratings",  
    title="Number of Ratings for the Highest Rated iPhones",
    labels={"Product Name": "iPhone Models", "Number Of Ratings": "Number of Ratings"}, 
    color="Number Of Ratings",  # Adds color differentiation based on rating count
    text_auto=True  # Displays values on bars for clarity
)

# Adding a trendline using scatter plot over the bars
fig.add_scatter(
    x=highest_rated["Product Name"], 
    y=highest_rated["Number Of Ratings"], 
    mode="lines+markers", 
    name="Trend Line", 
    line=dict(color="red", dash="dash")
)

# Updating layout for better readability
fig.update_layout(
    xaxis_title="iPhone Models",
    yaxis_title="Number of Ratings",
    legend_title="Legend",
    showlegend=True
)

fig.show()

# based on reviews
iphone=highest_rated["Product Name"].value_counts()
print(iphone)
labels=iphone.index
print(labels)
counts=highest_rated["Number Of Reviews"]
print(counts)

highest_rated = highest_rated.sort_values(by="Number Of Reviews", ascending=False)

# Creating an improved bar chart
fig = px.bar(
    highest_rated, 
    x="Product Name", 
    y="Number Of Reviews",  
    title="Number Of Reviews for the Highest Rated iPhones",
    labels={"Product Name": "iPhone Models", "Number Of Reviews": "Number of Reviews"}, 
    color="Number Of Reviews",  # Adds color differentiation based on rating count
    text_auto=True  # Displays values on bars for clarity
)

# Adding a trendline using scatter plot over the bars
fig.add_scatter(
    x=highest_rated["Product Name"], 
    y=highest_rated["Number Of Reviews"], 
    mode="lines+markers", 
    name="Trend Line", 
    line=dict(color="red", dash="dash")
)

# Updating layout for better readability
fig.update_layout(
    xaxis_title="iPhone Models",
    yaxis_title="Number of Reviews",
    legend_title="Legend",
    showlegend=True
)

fig.show()

# SALES PRICE
# fig1=px.scatter(df,x="Sale Price",y="Number Of Ratings",size="Discount Percentage",trendline="ols",
#                 title="Relationship between sales price and number of rating")
# fig1.show()

#or

import plotly.express as px

# Creating the scatter plot with trendline
fig1 = px.scatter(
    df, 
    x="Sale Price", 
    y="Number Of Ratings", 
    size="Discount Percentage", 
    trendline="ols",  # Adding Ordinary Least Squares (OLS) regression line
    title="Relationship Between Sale Price and Number of Ratings",
    color="Discount Percentage",  # Color points based on discount percentage
    text=df["Discount Percentage"],  # Show discount percentage on hover
)

# Improve layout for better readability
fig1.update_layout(
    xaxis_title="Sale Price (INR)",  
    yaxis_title="Number of Ratings",
    legend_title="Discount Percentage (%)",
    showlegend=True,
    template="plotly_white",  # Light background for clarity
)

# Improve marker visibility
fig1.update_traces(
    marker=dict(opacity=0.7, line=dict(width=1, color="DarkSlateGrey"))  # Adjust marker transparency & border
)

fig1.show()


# fig 3

# fig2=px.scatter(df,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",
#                 trendline="ols",title="Relationship between discount percentage and number of rating"
                
#         )

# fig2.show()
import plotly.express as px

# Creating the scatter plot with trendline
fig2 = px.scatter(
    df, 
    x="Number Of Ratings", 
    y="Discount Percentage", 
    size="Sale Price", 
    trendline="ols",  # Adding Ordinary Least Squares (OLS) regression line
    title="Relationship Between Discount Percentage and Number of Ratings",
    color="Sale Price",  # Color points based on sale price for better visualization
    text=df["Sale Price"],  # Show sale price on hover
)

# Improve layout for better readability
fig2.update_layout(
    xaxis_title="Number of Ratings",  
    yaxis_title="Discount Percentage (%)",
    legend_title="Sale Price (INR)",
    showlegend=True,
    template="plotly_white",  # Light background for clarity
)

# Improve marker visibility
fig2.update_traces(
    marker=dict(opacity=0.7, line=dict(width=1, color="DarkSlateGrey"))  # Adjust marker transparency & border
)

fig2.show()
















 