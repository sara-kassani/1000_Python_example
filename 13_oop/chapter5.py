# Module 5: Classes Attributes
# use the built-in functions getattr() and print () to display the values of the given attributes

class Phone:
    brand= 'Iphone'
    model= 'Iphone X'

print(getattr(Phone, 'brand'))
print(getattr(Phone, 'model'))
                # Iphone
                # Iphone X

# Using dot notation, modify the value of the attributes, print the values for the brand and model attributes
class Phone:
    brand= 'Apple'
    model= 'iphone X'

Phone.brand= 'Samsung'
Phone.model= 'Galaxy'

print(f'brand: {Phone.brand}')
print(f'model: {Phone.model}')

                # brand: Samsung
                # model: Galaxy

# Use the setattr( ) built-in function modify the value of attributes, using the built-in function getattr() and print()
class Laptop:
    brand= 'Lenovo'
    model= 'ThinkPad'

setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print(f"brand: {getattr(Laptop, 'brand')}")
print(f"model:{getattr(Laptop, 'model')}")

print()

# Display all user-defined class attribute names with their values
class Onlineshop:
    sector= 'Electronics'
    sector_code= 'ELE'
    is_public_company= False

for attr, value in Onlineshop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

            # sector -> Electronics
            # sector_code -> ELE
            # is_public_company -> False

print("'{:^12}'".format("*****"))

# create describe_attrs() function to display all user-defined class attribute names with their values
class Onlineshop:
    sector= 'Electronics'
    sector_code= 'ELE'
    is_company_public= False

def describe_attrs():
    for attr, value in Onlineshop.__dict__.items():
        if not attr.startswith("_"):
            print(f'{attr} -> {value}')

describe_attrs()

print("'{:^12}'".format("*****"))
class HouseProject:
    number_of_floors = 3
    area = 1000
    def describe_project():
        print(f"Floor number: {HouseProject.number_of_floors}\n Area: {HouseProject.area}")

HouseProject.describe_project()
                    # Floor number: 3
                    #  Area: 1000