
import wallet
import portfolio

class Investor:
    def __init__(self, name):
        self.name = name
        self.wallet = wallet.Wallet(0)
        self.portfolio = portfolio.Portfolio()

    def investor_details(self):
        return {'Name': self.name, 'Wallet': self.wallet, 'Portfolio': self.portfolio}

    def __str__(self):
        return f'This is the account for investor: {self.name}'

    def __repr__(self):
        return f'This is the account for investor: {self.name}'

    def see_wallet(self):
        print(f'The wallet balance for investor {self.name} is: {str(self.wallet)}')

    def see_portfolio(self):
        print(f'Investor {self.name} has a portfolio of: {str(self.portfolio)}')

