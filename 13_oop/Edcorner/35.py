class Pet:
    def __init__(self, name, age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
pet=Pet("Max", 5)
print(pet.__dict__)


"""
{'_name': 'Max', '_age': 5}
"""