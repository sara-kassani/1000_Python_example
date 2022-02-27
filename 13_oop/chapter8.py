# Module 8 Encapsulation

    # _member is protected:  members of a class that can be accessed within the class and the classes derived from that class
    # __member is private

class Laptop:
    def __init__(self, price):
        self._price=price     #  protected attribute

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

laptop= Laptop(3499)
print(laptop.get_price())    #  3499

laptop.set_price(5499)
print(laptop.get_price())    #  5499

print("{:^12}".format("*****" * 10))
# @property decorator: makes usage of getter and setters much easier in Object-Oriented Programming
# (read-only properties)

class Pet:
    def __init__ (self, name):
        self._name = name

    @property
    def name(self):
        return self._name

pet=Pet('MAX')
print(pet.__dict__)     #   {'_name': 'MAX'}

print("{:^12}".format("*****" * 10))
# Implement a class named Pet that has two protected instance attributes:
# name and age, respectively. Next implement the methods: name() and age(),
# which reads the value of the protected attributes: name and age.

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

pet = Pet('MAX', 5)
print(pet.__dict__)
                    # {'_name': 'MAX', '_age': 5}

print("{:^12}".format("*****" * 10))
# (property to read and modify, without validation)

class Pet:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

pet = Pet('Max')
pet.name = 'Oscar'

print(pet.__dict__)
                        # {'_name': 'Oscar'}