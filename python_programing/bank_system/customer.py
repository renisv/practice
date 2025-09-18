from account import Account

class Customer:
    def __init__(self, name, account):
        if type(account) is not Account:
            raise TypeError("account must be an instance of Account class")
        self.account = account
        self.name = name

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.account.balance

    def __str__(self):
        return f"Customer: {self.name}, Balance: ${self.get_balance():.2f}"