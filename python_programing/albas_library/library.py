from book import Book

class Library:
    def __init__(self):
        self.__book_list = []

    @property
    def book_list(self):
        return self.__book_list
    
    def print_books(self):
        for book in self.book_list:
            print(book)

    def add_book(self, book):
        if type(book) is not Book:
            raise TypeError("You can only add Book objects")
        self.__book_list.append(book)

    def remove_book(self, book_ISBN):
        position = self.search_by_ISBN(book_ISBN)
        if position == -1:
            print("Book not found")
            return
        self.book_list.pop(position)
        


    def search_by_ISBN(self, book_ISBN):
        position = -1
        for i in range(len(self.book_list)):
            if self.book_list[i].ISBN == book_ISBN:
                position = i
        return position

    def search_by_title(self, book_title):
        position = -1
        for i in range(len(self.book_list)):
            if self.book_list[i].ISBN == book_title:
                position = i
        return position


    def update_availablity(self, borrow, book_ISBN):
        position = self.search_by_ISBN(book_ISBN)
        book = self.book_list[position]

        if borrow == 1:
            if book.available_copies == 0:
                print("No copies left to borrow")
            book.available_copies -= 1
        elif borrow == 0:
            book.available_copies += 1
        return book.available_copies
        
    