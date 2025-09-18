from library import Library
from book import Book

class LibraryMenu:
    def __init__(self):
        self.library = Library()
        self.initialize_sample_books()
    
    def initialize_sample_books(self):
        # Add some sample books
        books = [
            Book("Harry Potter", "J.K. Rowling", "9780439708180", 5, 4),
            Book("The Hobbit", "J.R.R. Tolkien", "9780547928227", 4, 2),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 6, 1),
            Book("1984", "George Orwell", "9780451524935", 3, 0),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 5, 2)
        ]
        for book in books:
            self.library.add_book(book)
    
    def display_menu(self):
        print("\n" + "="*40)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. View all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Search by ISBN")
        print("5. Search by title")
        print("6. Borrow a book")
        print("7. Return a book")
        print("8. Sort by author")
        print("9. Sort by title")
        print("10. Exit")
        print("="*40)
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-10): ").strip()
            
            if choice == "1":
                self.view_all_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.remove_book()
            elif choice == "4":
                self.search_by_isbn()
            elif choice == "5":
                self.search_by_title()
            elif choice == "6":
                self.borrow_book()
            elif choice == "7":
                self.return_book()
            elif choice == "8":
                self.sort_by_author()
            elif choice == "9":
                self.sort_by_title()
            elif choice == "10":
                print("Thank you for using the Library System!")
                break
            else:
                print("Invalid choice! Please enter a number from 1 to 10.")
    
    def view_all_books(self):
        print("\n--- ALL BOOKS IN LIBRARY ---")
        self.library.print_books()
    
    def add_book(self):
        print("\n--- ADD NEW BOOK ---")
        try:
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN (13 digits): ").strip()
            total = int(input("Enter total copies: "))
            available = int(input("Enter available copies: "))
            
            new_book = Book(title, author, isbn, total, available)
            self.library.add_book(new_book)
            print(f"Book '{title}' added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error adding book: {e}")
    
    def remove_book(self):
        print("\n--- REMOVE BOOK ---")
        isbn = input("Enter ISBN of book to remove: ").strip()
        self.library.remove_book(isbn)
    
    def search_by_isbn(self):
        print("\n--- SEARCH BY ISBN ---")
        isbn = input("Enter ISBN to search: ").strip()
        position = self.library.search_by_ISBN(isbn)
        if position != -1:
            book = self.library.book_list[position]
            print("Book found:")
            print(book)
            print(f"Available copies: {book.available_copies}/{book.total_copies}")
        else:
            print("Book not found!")
    
    def search_by_title(self):
        print("\n--- SEARCH BY TITLE ---")
        title = input("Enter title to search: ").strip()
        position = self.library.search_by_title(title)
        if position != -1:
            book = self.library.book_list[position]
            print("Book found:")
            print(book)
            print(f"Available copies: {book.available_copies}/{book.total_copies}")
        else:
            print("Book not found!")
    
    def borrow_book(self):
        print("\n--- BORROW BOOK ---")
        isbn = input("Enter ISBN of book to borrow: ").strip()
        try:
            result = self.library.update_availablity(1, isbn)
            if result is not False:
                print("Book borrowed successfully!")
        except Exception as e:
            print(f"Error: {e}")
    
    def return_book(self):
        print("\n--- RETURN BOOK ---")
        isbn = input("Enter ISBN of book to return: ").strip()
        try:
            result = self.library.update_availablity(0, isbn)
            if result is not False:
                print("Book returned successfully!")
        except Exception as e:
            print(f"Error: {e}")
    
    def sort_by_author(self):
        print("\n--- BOOKS SORTED BY AUTHOR ---")
        sorted_books = self.library.sort_by_author()
        for book in sorted_books:
            print(book)
    
    def sort_by_title(self):
        print("\n--- BOOKS SORTED BY TITLE ---")
        sorted_books = self.library.sort_by_title()
        for book in sorted_books:
            print(book)