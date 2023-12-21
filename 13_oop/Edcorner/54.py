class Person:
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age

class Department:
    def __init__(self, dept_name, short_dept_name):
        self.dept_name=dept_name
        self.short_dept_name=short_dept_name

class Worker(Person, Department):
    def __init__(self, fname, lname, age, dept_name, short_dept_name):
        Person.__init__(self, fname, lname, age)
        Department.__init__(self, dept_name, short_dept_name)


worker=Worker("John", "Doe", 30, "Information Technology", "IT")
print(worker.__dict__)

"""
{'fname': 'John', 'lname': 'Doe', 'age': 30, 'dept_name': 'Information Technology', 'short_dept_name': 'IT'}
"""