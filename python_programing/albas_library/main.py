from book import Book
from library import Library

first_book = Book("Harry Potter", "J.K. Rowling", "9780439708180", 5, 4)
second_book = Book("The Hobbit", "A.R.R. Tolkien", "9780547928227", 4, 2)
third_book = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 6, 1)
fourth_book = Book("1984", "George Orwell", "9780451524935", 3, 0)
fifth_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 5, 2)

library = Library()

library.add_book(first_book)
library.add_book(second_book)
library.add_book(third_book)
library.add_book(fourth_book)
library.add_book(fifth_book)

library.print_books()
print()

library.sort_by_author()

library.print_books()