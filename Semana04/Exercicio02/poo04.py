import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not a accepted value"
        assert quantity >= 0, f"Quantity {quantity} is not a accepted value" 
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        else:
            return False        
    
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"
        
print(Item.is_integer(7.5))