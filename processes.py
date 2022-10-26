def get_action():
    print('What would you like to do (please input number)?')
    action = int(input(
        f'1. Create Account\n2. Add/Withdraw money from Wallet\n3. View a stock\n4. Buy/Sell a stock\n5. View Portfolio\n6. Exit program\n'))
    return action

def validate_action(action):
    if action not in [1, 2, 3, 4, 5, 6]:
        raise Exception('Incorrect input, please type a 1,2,3,4,5 or 6')

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
