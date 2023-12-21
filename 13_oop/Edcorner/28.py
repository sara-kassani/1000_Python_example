"""
Implement a method in the Laptop class called dispiay_private_attrs( ) that displays the names of all private
attributes of the instance. Then create an instance with the given arguments:
• 'Acer'
• 'Predator'
• 'AC-100'
• 5490
• 0.2
and assign it to the variable laptop. 

1. call dispiay_private_attrs() on the laptop instance
2. Implement a method called dispiay_private_attrs( ) that displays the names of all protected attributes
of the instance. 
"""

class Laptop:
    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f"_{self.__class__.__name__}__"):
                print(attr)

    def display_protected_attrs(self):
        for attr in self.__dict__:
            if attr.startswith("_") and not attr.startswith(f"_{self.__class__.__name__}"):
                print(attr)


laptop= Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()

"""
_Laptop__price
_Laptop__margin
"""

laptop.display_protected_attrs()

"""
_model
_code
"""