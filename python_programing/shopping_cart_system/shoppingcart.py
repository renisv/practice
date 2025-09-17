from product import Product

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_product(self, product):
        self.__items.append(product)

    def remove_product(self, product_name):
        for item in self.__items:
            if item.name == product_name:
                self.__items.remove(item)
                break

    def total_price(self):
        total = 0
        for item in self.__items:
            total += item.price
        return total

    def __str__(self):
        items_list = "\n".join([str(item) for item in self.__items])
        return f"Items in cart:\n{items_list}\nTotal: ${self.total_price():.2f}"

    def __dict__(self):
        return {
            "items": [item.__dict__() for item in self.__items],
            "total": self.total_price()
        }