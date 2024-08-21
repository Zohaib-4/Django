class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price =self.total_price + price
    
    def remove_item(self, item, price):
        self.items.remove(item)
        self.total_price =self.total_price - price

    def checkout(self):
        if self.total_price == 0:
            return "Your cart is empty"
        else:
            return f"Total Price: {self.total_price}"
        
cust1 = ShoppingCart()
cust1.add_item("Laptop", 1200)
cust1.add_item("HeadPhone", 400)
cust1.remove_item("HeadPhone",400)

print(cust1.checkout())