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
import wallet
class Portfolio:
    def __init__(self):
        self.position = {}

    def Buy(self):
        tickerSymbol = input('What stock (ticker symbol) would you like to buy? ')
        buystock = Stock(tickerSymbol)
        currentprice = buystock.get_current_price()
        quantity = input(f'How much of {buystock} (Current price: {currentprice}) would you like to buy? ')
        amount = round(float(currentprice) * float(quantity), 2)
        if tickerSymbol not in self.position:
            self.position[tickerSymbol] = amount
        else:
            self.position[tickerSymbol] += amount

    def Sell(self):
        tickerSymbol = input(f'Which of the following positions: {self.position} would you like to sell? ')
        sellstock = Stock(tickerSymbol)
        currentprice = sellstock.get_current_price()
        quantity = input(f'How much of {sellstock} (Current position: {self.position[tickerSymbol]} would you like to sell? ')
        amount = round(float(currentprice) * float(quantity), 2)
        if tickerSymbol not in self.position:
            return 'You do not own that stock!'
        elif amount > self.position[tickerSymbol]:
            return f'Insufficient stock to execute trade!'
        else:
            self.position[tickerSymbol] -= amount

    def __str__(self):
        return str(self.position)
        # a = ''
        # for keys, value in self.position.items():
        #     a += f'stock {keys} has balance of {value}\n'
        # return a

    def __repr__(self):
        return str(self.position)
        # a = ''
        # for keys, value in self.position.items():
        #     a += f'stock {keys} has balance of {value}\n'
        # return a

