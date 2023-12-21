"""
Implement a class called Laptop that sets the following instance attributes when creating an instance:
• brand
• model
• price

Then create an instance named laptop with the following attribute values:
• brand = 'Acer'
• model = 'Predator'
• price = 5490

- Use the special method init
- Implement a method in the Laptop class called display_instance_attrs() that displays the names of all the
attributes of the Laptop instance.
"""

class Laptop:
    def __init__(self, brnad, model, price):
        self.brand= brnad
        self.model= model
        self.price= price


    def display_instance_attrs(self):
        for attr in self.__dict__.keys():
            print(attr)

    def display_instance_attrs_with_values(self):
        for attr in self.__dict__.keys():
            print(f"{attr} -> {getattr(self, attr)}")


laptop= Laptop("Acer", "Predator", 5490)

laptop.display_instance_attrs()
"""
brand
model
price
"""
laptop.display_instance_attrs_with_values()
"""
brand -> Acer
model -> Predator
price -> 5490
"""