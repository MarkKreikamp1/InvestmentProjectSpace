""""
Script for functions on how an investor can interact with stocks. These functions include:

-> Buy/Sell
-> Stop Loss
-> Options
-> Limit orders
-> Stop-Loss
-> Stop-Limit

Script created: Greg Paterson
"""
import requests

def get_stock_data(stock_ticker, interval=5):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock_ticker + '&interval=' + str(interval) + 'min&apikey=X266B0IXMXQ7IN5J'
    r = requests.get(url)
    data = r.json()
    return data

class Portfolio:
    def __init__(self):
        self.position = {}

    def Buy(self, tickerSymbol, quantity):
        data = get_stock_data(tickerSymbol, interval=5)
        lastestDate = max(list(data[f'Time Series (5min)']))
        closeprice = data[f'Time Series (5min)'][lastestDate]['4. close']
        if tickerSymbol not in self.position:
            self.position[tickerSymbol] = round(float(closeprice) * float(quantity),2)
        else:
            self.position[tickerSymbol] += round(float(closeprice) * float(quantity), 2)

    def Sell(self, tickerSymbol, quantity):
        data = get_stock_data(tickerSymbol, interval=5)
        lastestDate = max(list(data[f'Time Series (5min)']))
        closeprice = data[f'Time Series (5min)'][lastestDate]['4. close']
        if tickerSymbol not in self.position:
            return 'You do not own that stock!'
        elif float(closeprice) * float(quantity) > self.position[tickerSymbol]:
            return f'Insufficient stock to execute trade!'
        else:
            self.position[tickerSymbol] -= round(float(closeprice) * float(quantity), 2)

    def __str__(self):
        a = ''
        for keys, value in self.position.items():
            a += f'stock {keys} has balance of {value}\n'
        return a

    def __repr__(self):
        a = ''
        for keys, value in self.position.items():
            a += f'stock {keys} has balance of {value}\n'
        return a