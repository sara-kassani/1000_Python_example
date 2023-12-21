"""
Encapsulation
"""

class Laptop:
    def __init__(self, price):
        self._price=price
    
    def get_price(self):
        return self._price
    
    def set_price(self, value):
        self._price=value


laptop= Laptop(3499)
print(laptop.get_price())

laptop.set_price(4500)
print(laptop.get_price())


"""
3499
4500
"""