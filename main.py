# main.py
from account import Account
from transaction import Transaction

# Create accounts
account1 = Account("12345", 1000.0)
account2 = Account("67890", 500.0)

# Display initial account information
account1.display_info()
account2.display_info()

# Perform transactions
Transaction.transfer(account1, account2, 200.0)

# Display updated account information
account1.display_info()
account2.display_info()
