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
- Print the value of the _dict_ attribute of the laptop instance.
"""


class Laptop:
    def __init__(self, brnad, model, price):
        self.brand= brnad
        self.model= model
        self.price= price

laptop= Laptop("Acer", "Predator", 5490)

print(laptop.__dict__)



"""
{'brand': 'Acer', 'model': 'Predator', 'price': 5490}
"""