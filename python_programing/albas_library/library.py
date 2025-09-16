from book import Book

class Library:
    def __init__(self):
        self.__book_list = []

    @property
    def book_list(self):
        return self.__book_list
    
    def add_book(self, book):
        self.__book_list.append(book)

    def print_books(self):
        for book in self.__book_list:
            print(book)

    