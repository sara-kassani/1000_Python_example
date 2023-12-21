"""use the built-in functions getattr() and print () to display the values of the given attributes of the class"""

class Phone():

    brand= "Apple"
    model= "Iphone X"


print(getattr(Phone, 'brand'))
print(getattr(Phone, 'model'))


"""
Apple
Iphone X
"""
