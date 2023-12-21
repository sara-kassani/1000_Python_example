"""
Implement a class named Pet that has one protected instance attribute name. 
Then implement a method name( ) which reads the value of the protected name attribute.
Create a property name (read-only) using the @property decorator.
Create an instance of the Pet class named pet and set name attribute to 'Max' . 
print the contents of the _dict_ attribute of this instance.
"""

class Pet:
    def __init__(self, name):
        self._name= name
    
    @property
    def name(self):
        return self._name
    
pet= Pet("Max")
print(pet.__dict__)

{'_name': 'Max'}


"""
@property decorator:
- Encapsulation
- Getter Method: The @property decorator is used to define a getter method. 
- Read-Only Attribute: Since you have not defined a setter for the name property, 
this makes name a read-only attribute. Attempting to set pet.name = "New Name" will raise an AttributeError.

"""
#===================================================
## same code without using @property

class Pet:
    def __init__(self, name):
        self._name = name

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, value):
        self._name = value

pet = Pet("Max")
print(pet.get_name())  # Accessing name using getter method

pet.set_name("Buddy")  # Modifying name using setter method
print(pet.get_name())  # Accessing name again to see the change


