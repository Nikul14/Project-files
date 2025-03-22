# You are given a dataset containing the monthly revenue (in USD) of an e-commerce company for the past 12 months. Your task is to compute the following statistical measures:

# Mean – The average revenue.

# Median – The middle revenue value.

# 25th, 50th, and 75th Percentiles – The values below which 25%, 50%, and 75% of the data fall.'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
revenue={
    "name":["john","kroll",'mohan',"sham","geeta","a","b","c","d","e","f","g","h","i","j","k"],
    "income":[42000, 38000, 50000, 47000, None, 53000, 55000, 60000, 
            62000, 58000, 57000, 59000, 61000, 150000, 2000, None]}
df=pd.DataFrame(revenue)
print(df)
print(df.info())
df["income"].fillna(df["income"].median(),inplace=True) #missing value handle with median
print(df["income"])

# Outlier Detection 
 
lower_percentile = df["income"].quantile(0.10)  # 10th percentile
upper_percentile = df["income"].quantile(0.90)  # 90th percentile

# Replace outliers with respective percentiles
df["income"] = df["income"].apply(lambda x: lower_percentile if x < lower_percentile 
                                  else upper_percentile if x > upper_percentile 
                                  else x)
print(df)

# visualization 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data dictionary
revenue = {
    "name": ["john", "kroll", "mohan", "sham", "geeta", "a", "b", "c", "d", "e", 
             "f", "g", "h", "i", "j", "k"],
    "income": [42000, 38000, 50000, 47000, None, 53000, 55000, 60000, 
               62000, 58000, 57000, 59000, 61000, 150000, 2000, None]
}

# Create DataFrame
df = pd.DataFrame(revenue)

# Check for missing values
print(df.info())

# Handle missing values using the median
df["income"].fillna(df["income"].median(), inplace=True)

# Outlier Detection using Percentiles
lower_percentile = df["income"].quantile(0.10)  # 10th percentile
upper_percentile = df["income"].quantile(0.90)  # 90th percentile

# Replace outliers with respective percentiles
df["income"] = df["income"].apply(lambda x: lower_percentile if x < lower_percentile 
                                  else upper_percentile if x > upper_percentile 
                                  else x)

# Display cleaned data
print(df)

# Boxplot to show income distribution after outlier handling
plt.figure(figsize=(8, 4))
plt.boxplot(df["income"], vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title("Income Distribution After Replacing Outliers with Percentiles")
plt.xlabel("Income")
plt.show()



