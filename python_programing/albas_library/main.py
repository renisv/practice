from menu import LibraryMenu

def main():
    print("Welcome to the Library Management System!")
    print("Initializing library with sample books...")
    
    
    menu = LibraryMenu()
    menu.run()

if __name__ == "__main__":
    main()