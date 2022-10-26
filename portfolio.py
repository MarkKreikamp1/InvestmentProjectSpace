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
from Portfolio.Stocks.stock import Stock
class Portfolio:
    def __init__(self):
        self.position = {}

    def buy(self):
        buystock = Stock()
        tickerSymbol = buystock.ticker
        currentprice = buystock.get_current_price()
        quantity = input(f'How much of {buystock} (Current price: {currentprice}) would you like to buy? ')
        if tickerSymbol not in self.position:
            self.position[tickerSymbol] = round(float(currentprice) * float(quantity),2)
        else:
            self.position[tickerSymbol] += round(float(currentprice) * float(quantity), 2)

    def Sell(self):
        sellstock = Stock()
        tickerSymbol = sellstock.ticker
        currentprice = sellstock.get_current_price()
        quantity = input(f'How much of {sellstock} (Current position: {self.position[tickerSymbol]} would you like to sell? ')
        if tickerSymbol not in self.position:
            return 'You do not own that stock!'
        elif float(currentprice) * float(quantity) > self.position[tickerSymbol]:
            return f'Insufficient stock to execute trade!'
        else:
            self.position[tickerSymbol] -= round(float(currentprice) * float(quantity), 2)

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


