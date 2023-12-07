# transaction.py
class Transaction:
    @staticmethod
    def transfer(sender, receiver, amount):
        if 0 < amount <= sender.get_balance():
            sender.withdraw(amount)
            receiver.deposit(amount)
            print(f"Transferred ${amount:.2f} from account {sender.get_account_number()} "
                  f"to account {receiver.get_account_number()}")
        else:
            print(f"Invalid transfer from account {sender.get_account_number()} "
                  f"to account {receiver.get_account_number()}")
