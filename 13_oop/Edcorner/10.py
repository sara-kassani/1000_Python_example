""" Using dot notation, modify the value of the attributes """

class Phone:
    brand= "Apple"
    model= "Iphone X"

Phone.brand= "Samsung"
Phone.model= "Galaxy"

print(f"brand: {Phone.brand}")
print(f"model: {Phone.model}")

"""
brand: Samsung
model: Galaxy
"""
