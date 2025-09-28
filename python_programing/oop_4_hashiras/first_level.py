"""class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

    def get_summary(self):
        return f"The book title is {self.title} and it is written by {self.author}."

    def __str__(self):
        return f"Book title: {self.title}    Author: {self.author}"


class Textbook(Book):
    def __init__(self, title, author, pages, subject):
        super().__init__(title, author, pages)
        self.subject = subject
    
    def get_summary(self):
        return f"The book subject is {self.subject} and it is written by {self.author}."
    



first_book = Book("Chalkman", "Tudor", 277)
second_book = Textbook("Kulturat", "Valbona", 344, "biotech")
print(first_book)
print(second_book)
print(first_book.is_long())
print(second_book.is_long())"""


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount

    
account_holder = BankAccount(300)
account_holder.withdraw(250)
print(account_holder.balance)

