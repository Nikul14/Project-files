import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
 

# API Key & Stock Symbol
Api_key = "XLIJWATRV0S8SOY2"  #  my API_KEY
stock_symbol = "IBM"

#   the API
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&outputsize=compact&apikey={Api_key}"

# Fetch Data
response = requests.get(URL)
data = response.json()

# Print API Response
print(json.dumps(data, indent=4))

# JSON data to Pandas DataFrame
df=pd.DataFrame.from_dict(data["Time Series (Daily)"],orient="index")
df=df.astype(float)
df.index=pd.to_datetime(df.index)
df.columns= ["OPEN","HIGH","LOW","CLOSE","VOLUME"]
print(df.head())

# CLEANING DATA
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

# now visulalize
def plot_stock(df,column_name,title):
    plt.figure(figsize=(12,6))
    plt.plot(df.index,df[column_name],label=column_name)
    plt.xlabel("Date")
    plt.ylabel("Price(USD)")
    plt.grid()
    plt.legend()
    plt.show()
plot_stock(df,"CLOSE","stock  losing price over time")

# daily stock returns:
df["Daily Return"] = df["CLOSE"].pct_change()
print(df[["CLOSE", "Daily Return"]].head())

#  moving averages (7-day & 30-day):

df["7-Day MA"] = df["OPEN"].rolling(window=7).mean()
df["30-Day MA"] = df["OPEN"].rolling(window=30).mean()
print(df[["OPEN","7-Day MA","30-Day MA"]])


import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(df.index, df["CLOSE"], label="Closing Price", color='blue')
plt.plot(df.index, df["7-Day MA"], label="7-Day MA", color='red', linestyle="dashed")
plt.plot(df.index, df["30-Day MA"], label="30-Day MA", color='green', linestyle="dashed")

plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()


import plotly.express as px

fig = px.line(df, x=df.index, y="CLOSE", title="Stock Closing Price Over Time")
fig.show()


import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['OPEN'],
                high=df['HIGH'],
                low=df['LOW'],
                close=df['CLOSE'])])

fig.update_layout(title="Stock Candlestick Chart", xaxis_title="Date", yaxis_title="Price (USD)")
fig.show()

df.to_csv("Time series cleaned data")
