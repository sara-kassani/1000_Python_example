""" create a class and Display all _dict_ attribute keys of the class """

class Container:
    pass

print(Container.__dict__.keys())

""" dict_keys(['__module__', '__dict__', '__weakref__', '__doc__']) """