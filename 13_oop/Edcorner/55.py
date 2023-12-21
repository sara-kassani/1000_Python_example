class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
people= [Person("Tom", 25), Person("John", 29), Person("Mike", 27), Person("ALice", 19)]

people.sort(key=lambda person: person.age)

for person in people:
    print(f"{person.name} --> {person.age}")


"""
ALice --> 19
Tom --> 25
Mike --> 27
John --> 29
"""