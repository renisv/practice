class Book:
    def __init__(self, title, author, ISBN, total_copies, available_copies):

        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.total_copies = total_copies
        self.available_copies = available_copies

    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def ISBN(self):
        return self.__ISBN
    
    @property
    def total_copies(self):
        return self.__total_copies
    
    @property
    def available_copies(self):
        return self.__available_copies

    @title.setter
    def title(self, value):
        if type(value) is not str:
            raise TypeError("Book title can only be a string")
        if len(value) == 0:
            raise ValueError("Book title cant be empty")
        self.__title = value
    
    @author.setter
    def author(self, value):
        if type(value) is not str:
            raise TypeError("Author can only be a string")
        if len(value) == 0:
            raise ValueError("Author cant be empty")
        self.__author = value

    @ISBN.setter
    def ISBN(self, value):
        if type(value) is not str:
            raise TypeError("ISBN can only be a string")
        if len(value) != 13:
            raise ValueError("ISBN needs to be 13 digits")
        self.__ISBN = value

    @total_copies.setter
    def total_copies(self, value):
        if type(value) is not int:
            raise TypeError("Please enter a number")
        if value < 0:
            raise ValueError("Total cannot be negative")
        self.__total_copies = value
    
    @available_copies.setter
    def available_copies(self, value):
        if type(value) is not int:
            raise TypeError("Please enter a number")
        if value < 0:
            raise ValueError("Available copies cannot be negative")
        if value > self.total_copies:
            raise ValueError("Available copies cannot be more than total copies")
        self.__available_copies = value

    def __str__(self):
        return f"Book title: {self.title}, Author: {self.author}"