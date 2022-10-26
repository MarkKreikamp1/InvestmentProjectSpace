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
    # construct a requirement file

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
        # Look at/investigate available stocks -> Mark
            # historical value (1m/3m/1yr/3yr/5yr)
            # Optional: Financial Ratios
            # Optional: benchmarking (financial ratio's/performance based on segmentation(geographical/industry))
        # Buying -> Greg
            # stop loss
            # limit
        # sell -> Greg
            # stop loss
            # limit
    # wallet -> Bram
    # portfolio -> Bram
        # stock ticker
        # Base value
        # value changes over time
        # Optional: dividends (would relate to wallet)


#Step 1: Getting imports

import requests
import pandas as pd

#Step 2: Fetching the necessary data
from Portfolio.Stocks.stock import Stock
from portfolio import Portfolio
from wallet import Wallet

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


def run_program():
    p1 = Portfolio()
    w1 = Wallet('Test', 20000)
    while True:
        print('What would you like to do (please input number)?')
        action = int(input(f'1. Create Account\n2. Add/Withdraw money from Wallet\n3. View a stock\n4. Buy/Sell a stock\n5. View Portfolio\n6. Exit program\n'))
        if action not in [1, 2, 3, 4, 5, 6]:
            raise Exception('Incorrect input, please type a 1,2,3,4,5 or 6')
        if action == 1:
            p1 = Portfolio()
            print('Portfolio created successfully')
        elif action == 2:
            add_or_withdraw_money_from_wallet(w1)
        elif action == 3:
            pass
        elif action == 4:
            trade_operations(p1)
        elif action == 5:
            print(p1.__str__())
        else:
            print('Program Exit Successful')
            return


def trade_operations(p1):
    print('What would you like to do (please input number)?')
    operation = int(input(f'1. Buy\n2. Sell\n'))
    if operation == 1:
        p1.buy()
    else:
        p1.Sell()


def add_or_withdraw_money_from_wallet(w1):
    print(f'Current balance is {w1.balance}')
    print('What would you like to do (please input number)?')
    operation = int(input(f'1. Add cash\n2. Withdraw cash\n'))
    if operation == 1:
        amount_add = int(input(f'How much would you like to add?'))
        w1.add(amount_add)
        print(f"Succesfully added {amount_add} to wallet")
    else:
        amount_withdraw = int(input(f'How much would you like to withdraw?'))
        w1.withdraw(amount_withdraw)
        print(f"Succesfully removed {amount_withdraw} from wallet")


if __name__ == "__main__":
    run_program()











