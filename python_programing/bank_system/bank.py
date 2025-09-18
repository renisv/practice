from customer import Customer

class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer class")
        self.customers.append(customer)
        return f"Customer {customer.get_name()}

    def find_customer(self, name):
        for customer in self.customers:
            if customer.get_name().lower() == name.lower():
                return customer
        return None

    def get_total_balance(self):
        total = 0.0
        for customer in self.customers:
            total += customer.get_balance()
        return total

    def __str__(self):
        return f"Bank with {len(self.customers)} customers, Total balance: ${self.get_total_balance():.2f}"