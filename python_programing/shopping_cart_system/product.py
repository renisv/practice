class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Price of a product cannot be 0 or less")
        self.__price = price
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Product: {self.name} - Price: ${self.price:.2f}"
    
    def __dict__(self):
        return {"name": self.name, "price": self.price}