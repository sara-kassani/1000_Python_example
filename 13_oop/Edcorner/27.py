"""
Visibility of Variables

Implement a class called Laptop that sets the following instance attributes:

when creating an instance:
• brand as a bare instance attribute
• model as a protected attribute
• price as a private attribute

1- print the value of the _dict_ attribute of the laptop instance
2- print the value for each instance attribute
"""

class Laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model= model
        self.__price= price

laptop= Laptop('Acer', 'Predator', 5490)
##1
print(laptop.__dict__)

"""
{'brand': 'Acer', 'model': 'Predator', '_Laptop__price': 5490}
"""

##2
print(f"brand -> {laptop.brand}")
print(f"model -> {laptop.model}")
print(f"price -> {laptop._Laptop__price}")  ## Note here 

"""
brand -> Acer
model -> Predator
price -> 5490
"""