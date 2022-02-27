# Module 7: The _Init_() Method

class Laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price

laptop = Laptop('Acer', 'Predetor', 5490)
print(laptop.__dict__)    #  {'brand': 'Acer', 'model': 'Predetor', 'price': 5490}

print("{:^12}".format("*****" * 10))


class Laptop:
    def __init__ (self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    
    def display_instance_attrs(self):
        for attr in self.__dict__.keys():
            print(attr)

laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_instance_attrs()
                    # brand
                    # model
                    # price

print("{:^12}".format("*****" * 10))

class Laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price

    def display_attrs_with_values(self):
        for attr in self.__dict__.keys():
            print(f"{attr} --> {getattr(self, attr)}")

laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_attrs_with_values()
                    # brand --> Dell
                    # model --> Inspiron
                    # price --> 3699

print("{:^12}".format("*****" * 10))

class Vector:
    def __init__(self, *components):
        self.components=components
    
v1 = Vector(1, 3)
v2 = Vector(1, 3, 5, 9)

print(f"v1 -> {v1.components}")
print(f"v2 -> {v2.components}")
                    # v1 -> (1, 3)
                    # v2 -> (1, 3, 5, 9)

print("{:^12}".format("*****" * 10))

class Bucket:
    def __init__(self, **kwargs):
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)

bucket = Bucket(apple=3.5, milk=2.5, juice=1.5, water= 0.5)
print(bucket.__dict__)
                    # {'apple': 3.5, 'milk': 2.5, 'juice': 1.5, 'water': 0.5}

print("{:^12}".format("*****" * 10))

class Car:
    def __init__(self, brand, model, price, type_of_car = None):
        self.brand=brand
        self.model=model
        self.price=price
        self.type_of_car= type_of_car if type_of_car else 'Sedan'


car= Car('Opel', 'Insignia', 115000)
print(car.__dict__)
                     # {'brand': 'Opel', 'model': 'Insignia', 'price': 115000, 'type_of_car': 'Sedan'}

print("{:^12}".format("*****" * 10))
class Laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        if isinstance(price, (int, float)) and price > 0:
            self.price=price
        else:
            raise TypeError('The price attribute must be a positive int or float.')

laptop=Laptop('Acer', 'predator', 115000)
print(laptop.__dict__)

print("{:^12}".format("*****" * 10))

class Laptop:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        if isinstance(price, (int, float)) and price > 0:
            self.price=price
        else:
            raise TypeError('The price attribute must be a positive int or float.')

try:
    laptop=Laptop('Acer', 'Predetor', "115000")
except TypeError as error:
    print(error)
                        # The price attribute must be a positive int or float. 