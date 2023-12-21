class Pet:
    def __init__(self, name):
        self._name= name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=value

pet=Pet("Max")
pet.name='Oscar'

print(pet.__dict__)

"""
{'_name': 'Oscar'}
"""