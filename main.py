"""

Investment Game
#The goal of this project is to create an investment game, where people can buy virtual stock,
building an investment portfolio with virtual money, and watch its performance.

Functional requirements
#At the very least, your program should allow a user to buy stock and see how it performs over time. When time allows,
you will add more features. Some suggestions:

#Create different kinds of orders (buy, sell, limits, stop orders, etc.)
#A cash balance for the user. This will of course go down when stock is bought.
# Multiple users
# Multiple currencies
# Searching for funds (by symbol, market, currency, name, etc.)
# A user interface. Optional: Graphical/Web
# (Graphical) reporting of the performance of funds and the portfolio as a whole


#Technical requirements

# Stock prices are taken from an online source like https://www.alphavantage.co/.
# There's an example notebook that shows you how to call thisservice and use the data.
# You will use pandas DataFrames for the stock prices you retrieve from the web.
# You will write classes for other data, like user profiles, orders, the portfolio, etc.
# Currency data is represented as integers, in thousands of cents.
# Your program will run standalone as a script.
# You will use git for version control
# Each member of your group will create their own virtual environment (not shared on git).
#  Installed packages are determined by a Requirements file, which is shared on git.

"""

#Step 1: Getting imports

#Step 2: Fetching the necessary data
    #Essential / Basic
        # Stock name
        # Stock ticker
        # Stock price
    #Optionals
        # Company Name
        # Company Geography
        # Company Industry
        # Company Size
            # Nr of emps
            # other..
        # Company Financials
            # Annual / quarterly earnings

#step 3: start building basic functionality
    # stock interaction
        # Look at/investigate available stocks
            # historical value (1m/3m/1yr/3yr/5yr)
            # Optional: Financial Ratios
            # Optional: benchmarking (financial ratio's/performance based on segmentation(geographical/industry))
        # Buying
            # stop loss
            # limit
        # sell
            # stop loss
            # limit
    # wallet
    # portfolio
        # stock ticker
        # Base value
        # value changes over time
        # Optional: dividends (would relate to wallet)


#Step 1: Getting imports

import requests
import pandas as pd

#Step 2: Fetching the necessary data

"""
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
"""
#TODO: Menu of stocks to choose from and their tickers -> below HTML Load
# pretty printing of pandas dataframe
#pd.set_option('expand_frame_repr', False)
#pd.set_option("display.max_rows", None, "display.max_columns", None)

# There are 4 tables on the Wikipedia page
# we want the last table

#payload=pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
#hundred_tickers = payload[1]

#100 tickers
# for each ticker in 100tickers:

def input_ticker(stock_ticker, interval = 60):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock_ticker + '&interval=' + str(interval) +'min&apikey=X266B0IXMXQ7IN5J'
    r = requests.get(url)
    data = r.json()
    return data

#request user for input

response = str(input("Can you provide the stock you want?"))
intervalspec = input("At how many minutes interval do you want to see the price? 5, 10, or 60")

print(input_ticker(response, intervalspec))
















