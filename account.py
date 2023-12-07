# account.py
class Account:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} to account {self.account_number}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount:.2f} from account {self.account_number}")
        else:
            print(f"Insufficient funds in account {self.account_number}")

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance
