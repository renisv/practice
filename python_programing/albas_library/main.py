from book import Book
from library import Library

first_book = Book("Harry Potter", "J.K.R.", "1234567890123", 5, 3)
second_book = Book("Chalkman", "J.K.R.", "1234567890123", 5, 3)
library = Library()

library.add_book(first_book)
library.add_book(2)
library.print_books()
