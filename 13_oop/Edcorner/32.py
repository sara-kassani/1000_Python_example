class Person:
    def __init__(self, first_name):
        self._first_name= first_name

    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, value):
        self._first_name= value

    first_name= property(fget=get_first_name, fset=set_first_name)

person=Person("John")
person.set_first_name("Mike")
print(person.first_name)

"""
Mike
"""