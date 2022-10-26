class Wallet:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def add(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Can't deposit a negative amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient balance!")
        else:
            print("Can't withdraw non positive amount!")

    def __str__(self):
        return f'{self.balance}'
