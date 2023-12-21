"""Using the setattr( ) built-in function modify the value of attributes"""

class Laptop:
    brand = 'Lenovo'
    model= 'ThinkPad'

setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print(f"brand: {getattr(Laptop, 'brand')}")
print(f"model: {getattr(Laptop, 'model')}")


"""
brand: Acer
model: Predator
"""