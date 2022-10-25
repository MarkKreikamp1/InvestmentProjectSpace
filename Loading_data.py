#Step 1: Getting imports

import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

#Step 2: Fetching the necessary data

"""
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

#TODO: Menu of stocks to choose from and their tickers -> below HTML Load
# pretty printing of pandas dataframe

pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows", None, "display.max_columns", None)

# There are 4 tables on the Wikipedia page
# we want the last table

payload = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
hundred_tickers = payload[1]

#100 tickers
# for each ticker in 100tickers:

"""
#def request user for input

def get_input():
    stock = str(input("Can you provide the stock you want?"))
    intervalspec = input("At how many minutes interval do you want to see the price? 5 or 60")
    lookup_date = dt.datetime.strptime(input("What day of last week do you want to see the prices, following the %Y-%m-%d format?"), "%Y-%m-%d").date().isoformat()

    return stock, intervalspec, lookup_date

def input_ticker():
    stock_ticker, interval, lookup_date = get_input()
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock_ticker + '&interval=' + str(interval) +'min&apikey=X266B0IXMXQ7IN5J'
    r = requests.get(url)
    data = r.json()
    return data, interval, lookup_date

def time_series_fun():
    #we have given the user options to select different stock types, now we want to unpack that data into a time series graph, or something of the sort.

    stock_data, interval, lookup_date = input_ticker()

    time_series = []
    open_values = []
    #What do we want to select? The open at every hour
    for dates in stock_data[f"Time Series ({interval}min)"]:
        if dt.datetime.strptime(dates[0:10], "%Y-%m-%d").date().isoformat() == lookup_date:
            time_series.append(int(dates[11:13]))
            open_values.append(float(stock_data[f"Time Series ({interval}min)"][dates]['1. open']))

    print(time_series)
    print(open_values)
    return time_series, open_values, lookup_date



"""
stock_data, interval, lookup_Date = input_ticker()

    time_series = []
    open_values = []
    #What do we want to select? The open at every hour
    for dates in stock_data[f"Time Series ({interval}min)"]:
        print(dates)
        if dt.datetime.strptime(dates[0:10], "%Y-%m-%d").date().isoformat() == lookup_Date:
            time_series.append(int(dates[11:13]))
            open_values.append(float(stock_data[f"Time Series ({interval}min)"][dates]['1. open']))
 """

