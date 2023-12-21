class Pet:
    def __init__(self, name, age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name=value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age=value


pet=Pet("Max", 5)
print(pet.__dict__)

pet.name='Tom'
pet.age=8
print(pet.__dict__)

"""
{'_name': 'Max', '_age': 5}
{'_name': 'Tom', '_age': 8}
"""
        