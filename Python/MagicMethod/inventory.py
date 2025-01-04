class InventoryItem: 
    def __init__(self, name, quantity):
        self.name = name    
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.name}', quantity={self.quantity})"
    
    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError('cannot add item of different type')

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError('cannot subtract more than available')
        raise ValueError('cannot substract item of different type')

    def __mul__(self, factor):
        if isinstance(factor, ( int, float )):
            return InventoryItem(self.name, int( self.quantity * factor ))
        raise Exception('Multiplication factor must be a number')

    def __truediv__(self, factor):
        if isinstance(factor, ( int, float )) and factor != 0:
            return InventoryItem(self.name, int( self.quantity / factor ))
        raise Exception('Divide factor must be a number and not zero')
    
    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False

    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError('cannot compare item of different type')

    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError('cannot compare item of different type')

# Create a inventory item
item1 = InventoryItem('apple', 10)
item2 = InventoryItem('apple', 5)
item3 = InventoryItem('banana', 5)

# Adding quantities of the same item
result_add = item1 + item2
print(result_add)  # Output: InventoryItem(name='apple', quantity=15)

# Subtracting quantities of the same item
result_sub = item1 - item2
print(result_sub)  # Output: InventoryItem(name='apple', quantity=5)

result_mul = item1 * 2
print(result_mul)  # Output: InventoryItem(name='apple', quantity=20)

result_div = item1 / 2
print(result_div)  # Output: InventoryItem(name='apple', quantity=5)

result_eq = item1 == item2
print(result_eq)  # Output: True

result_lt = item1 < item2
print(result_lt)  # Output: False