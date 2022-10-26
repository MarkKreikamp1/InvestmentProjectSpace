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

import processes
from portfolio import Portfolio
from wallet import Wallet


def run_program():
    p1 = Portfolio()
    w1 = Wallet(20000)
    while True:
        action = processes.get_action()
        processes.validate_action(action)
        if action == 1:
            p1 = Portfolio()
            print('Portfolio created successfully')
        elif action == 2:
            processes.add_or_withdraw_money_from_wallet(w1)
        elif action == 3:
            pass
        elif action == 4:
            processes.trade_operations(p1)
        elif action == 5:
            print(p1.__str__())
        else:
            print('Program Exit Successful')
            return


if __name__ == "__main__":
    run_program()











