class Person:
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age

class Department:
    pass


class Worker(Person, Department):
    pass


worker= Worker("John", "Doe", 35)
print(worker.__dict__)

"""
{'fname': 'John', 'lname': 'Doe', 'age': 35}
"""