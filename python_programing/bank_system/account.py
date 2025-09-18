class Account:
    def __init__(self, balance):
        self.balance = balance
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
    
    def deposit(self, amount):
        if type(amount) is not int or float:
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if type(amount) is not int or float:
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -=amount
        return self.balance
    
    def __str__(self):
        return f"Account balance: ${self.balance:.2f}"