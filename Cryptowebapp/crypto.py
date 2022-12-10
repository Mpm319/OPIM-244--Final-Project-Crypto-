##run the app
###
from pandas import read_csv

from Cryptowebapp.alpha import API_KEY

#import Crypto_App
#import os

def format_usd(my_price):
  return f"${my_price:,.2f}"

def fetch_crypto_data(symbol):
  request_url =f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=CNY&apikey={API_KEY}&datatype=csv"

  df=read_csv(request_url)

  return df

if __name__=="__main__":
  
  print("CRYPTO REPORT...")

  symbol=input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
  print("SYMBOL:", symbol)

  df=fetch_crypto_data(symbol)

  print(df.columns)
  print(df.head())
  #breakpoint()

  #print data
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
  print("PERCENT CHANGE THIS PAST YEAR: ",pct_change)

  fig=px.scatter(df,x="timestamp",y="close (USD)",title="Daily Stock Prices ")
  fig.update_yaxes(tickprefix="$")
  fig.show()