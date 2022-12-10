# OPIM-244--Final-Project-Crypto-

# This code is a script that can be used to analyze cryptocurrency data. It takes in a crypto symbol (e.g. BTC, ETH, etc) from the user and uses the AlphaVantage API to get the CSV data of the daily prices associated with the symbol. After the data is retrieved, the code performs calculations to get the latest adjusted close, the average price and the average daily trading volume over the past year, and the percent change from the last year. Finally, it produces a plotly scatter plot of the daily stock prices.

##setup

Create and activate a virtual environment
cd ~ /Desktop/OPIM-244--Final-Project-Crypto-
conda create -n crypto-env python=3.8
conda activate crypto-env

pip install -r requirements.txt

#Configuration
obtain a api key from alpha vantage https://www.alphavantage.co/support/#api-key
and store than in the env file



##Usage
python Cryptowebapp/crypto.py 
python Cryptowebapp/crypto_starter.py

comand to run
python -m Cryptowebapp.crypto
python -m Cryptowebapp.crypto_starter 


FLASK_APP=<Crypto_App flask run


# Local environment Crypto-MMA

#Heroku config APP_ENV="Crypto"

