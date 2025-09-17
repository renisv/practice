from user import User
from product import Product
from shoppingcart import ShoppingCart

class Store:
    def __init__(self):
        self.products = [
            Product("Laptop", 1200.99),
            Product("Mouse", 25.50),
            Product("Keyboard", 75.00),
            Product("Monitor", 300.00)
        ]
        self.users = {}
        self.current_user = None
        self.current_cart = None

    def register_user(self, username):
        if username in self.users:
            print("Username already exists!")
            return False
        
        new_user = User(username)
        self.users[username] = {
            'user': new_user,
            'cart': ShoppingCart()
        }
        print("User registered successfully!")
        print(new_user)
        return True

    def show_products(self):
        print("\nAvailable Products:")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product}")

    def login_user(self, username):
        if username in self.users:
            self.current_user = username
            self.current_cart = self.users[username]['cart']
            print(f"Logged in as {username}")
            return True
        else:
            print("User not found!")
            return False

    def add_to_cart(self, product_index):
        try:
            product_index = int(product_index) - 1
            if 0 <= product_index < len(self.products):
                product = self.products[product_index]
                self.current_cart.add_product(product)
                print(f"Added {product.name} to cart!")
            else:
                print("Invalid product number!")
        except ValueError:
            print("Please enter a valid number!")

    def view_cart(self):
        if self.current_cart:
            print(self.current_cart)
        else:
            print("No active cart! Please login first.")

    def run(self):
        while True:
            print("\n1. Register User")
            print("2. Show Products")
            print("3. Login")
            print("4. Add Product to Cart")
            print("5. View Cart")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                username = input("Enter username: ")
                self.register_user(username)
                
            elif choice == "2":
                self.show_products()
                
            elif choice == "3":
                username = input("Enter username: ")
                self.login_user(username)
                
            elif choice == "4":
                if not self.current_user:
                    print("Please login first!")
                    continue
                self.show_products()
                product_choice = input("Enter product number to add: ")
                self.add_to_cart(product_choice)
                
            elif choice == "5":
                self.view_cart()
                
            elif choice == "6":
                print("Thank you for shopping!")
                break
                
            else:
                print("Invalid choice! Please try again.")