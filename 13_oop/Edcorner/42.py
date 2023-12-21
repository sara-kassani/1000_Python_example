"""
Define a Person class that takes two bare attributes: fname (first name) and Iname (last name).
Then implement the _repr_ ( ) special method to display a formal representation of the Person object
Add a special method _str_ () to return an informal
representation of an instance of the Person class
"""
class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

    # def __str__(self):
    #     return f"First name: {self.fname}\nLast name: {self.lname}"


person=Person("John", "Doe")
print(person)


## repr
"""
Person(fname='John', lname='Doe')
"""


## str
"""
First name: John
Last name: Doe
"""