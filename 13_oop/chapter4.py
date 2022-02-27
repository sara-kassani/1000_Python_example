# Display all _dict_ attribute keys of the Person class to the console.

class Person:
    """Documnetation for Person class"""
    pass

print(Person.__dict__.keys())
            # dict_keys(['__module__', '__doc__', '__dict__', '__weakref__'])
print(Person.__module__)
            # __main__

# check if the model is an instance of the Model class
class Model:
    pass
model = Model()

print(isinstance(model, Model))    # True



