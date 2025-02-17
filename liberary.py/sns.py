# import seaborn  as sns
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# var1=[1,2,3,4,5,6,7,8]
# var2=[8,7,6,5,4,3,2,1]
# df=pd.DataFrame({'key': var1 , 'key2': var2})
# sns.lineplot(x='key',y='key2',data=df)
# plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# # Creating DataFrame
var1 = [1, 2, 3, 4, 5, 6, 7, 8]
var2 = [8, 7, 6, 5, 4, 3, 2, 1]

df = pd.DataFrame({'key': var1, 'key2': var2})
print(df)

# # # Corrected lineplot syntax
sns.lineplot(x='key', y='key2', data=df)  # ✅ Remove quotes around df
plt.show()


# matplotlib
var1 = [1, 2, 3, 4, 5, 6, 7, 8]
var2 = [8, 7, 6, 5, 4, 3, 2, 1]
plt.plot( var1,var2)
plt.xlabel('num')
plt.ylabel('income')
plt.title('line_chart')
plt.show()
pd.sns.plt
df1=sns.load_dataset("penguins")
print(df1)
# sns.lineplot(x='bill_length_mm',y='flipper_length_mm ',data=df1)
# plt.show()

print(df1.columns)

df1.columns = df1.columns.str.strip()  # Removes spaces from column names

sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=df1,hue="sex")
plt.show()

df1=sns.load_dataset("penguins").head(20)
print(df1)
print(df1.columns)
df1.columns = df1.columns.str.strip()
sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=df1,hue="sex",color="royalblue",linewidth=2.5)
plt.title("This is a line chart related to penguins")
plt.grid()
plt.show()


# #BAR CHART

sns.barplot(x="bill_length_mm",y="flipper_length_mm",data=df1,hue="sex",color="royalblue",linewidth=2.5)
plt.title("This is a line chart related to penguins")
plt.grid()
plt.show()

group_by= df1.groupby('island').size().reset_index(name="count")
print(group_by)
print(df1["island"])
print(df1.dtypes)
index = df1[df1.dtypes[df1.dtypes=='str'].index]
print(index)
print(df1.describe)


sns.barplot(x="species",y="island",data=df1,palette="pastel",hue="sex",linewidth=4)
plt.title("This is a bar chart related to penguins")
plt.show()


sns.barplot(x="species", y="island", data=df1, hue="sex", 
            palette=["#FF5733", "#33FF57"], linewidth=2.5)
plt.show()

# Histogram as dist.
sns.histplot(df1["island"],hue="sex", bins=20, kde=True, 
             palette="Set2", edgecolor="black", alpha=0.7)

plt.title("Distribution of Island Measurements by Sex", fontsize=14, fontweight='bold')
plt.xlabel("Island Measurement (mm)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend(title="Sex", fontsize=10)
plt.grid(axis='y', linestyle="--", alpha=0.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
sns.despine()  # Removes top & right borders

plt.show()