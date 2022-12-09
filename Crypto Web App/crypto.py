##run the app

import os

from pandas import read_csv
from getpass import getpass
import plotly.express as px


API_KEY = getpass("Please input your AlphaVantage API Key: ") 

symbols = ["BTC", "ETH", "ADA", "DOT", "XRP" , "XMR", "LTC", "BCH", "DOGE", "MATIC"  , "ATOM" ]

symbol = ""

while symbol not in symbols:
  print("Please make sure you applied the ticker correctly. You have to choose from: BTC, ETH")
  symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
  symbol=symbol.upper()

print("SYMBOL:", symbol)

request_url =f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=CNY&apikey={API_KEY}&datatype=csv"



df=read_csv(request_url)

print("Column names:", list(df.columns))
print("Number of rows:",len(df))

price_now = df.iloc[0]
print("LATEST ADJUSTED CLOSE: ", to_usd( price_now['close (USD)']))

last_year_df = df.head(365)
avg_price = to_usd(last_year_df['close (USD)'].mean())
avg_volume = last_year_df['volume'].mean()
print("AVERAGE PRICE THIS PAST YEAR: ", avg_price)
print("AVERAGE DAILY TRADING VOLUME THIS PAST YEAR: ",avg_volume)

price_ly = last_year_df.iloc[-1]['close (USD)']
price_now = last_year_df.iloc[0]['close (USD)']
pct_change = to_pct((price_now - price_ly) / price_ly)

#print(price_ly)
#print(price_now)
print("PERCENT CHANGE THIS PAST YEAR: ",pct_change)

fig=px.scatter(df,x="timestamp",y="close (USD)",title="Daily Stock Prices ")
fig.update_yaxes(tickprefix="$")
fig.show()