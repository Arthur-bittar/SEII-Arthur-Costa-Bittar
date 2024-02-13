class Item:
    def __init__(self, name: str, price: float, quantity: int):
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not a accepted value"
        assert quantity >= 0, f"Quantity {quantity} is not a accepted value" 
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        print(f"An instance created: Name: {name} , Price: {price} , Quatity: {quantity}")
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)


