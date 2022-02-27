# Implement a function called stick( ) that takes any number of bare arguments and return an object of
# type str being a concatenation of all arguments of type str passed to the function with the '#' sign.


def stick(*args):
    args=[arg for arg in args if isinstance(arg, str)]
    result= '#'.join(args)
    return result

print(stick('sport', 'summer', 'swim'))    #  sport#summer#swim
print(stick(3, 5, 7, 9)) # nothing is returned because the input args are not str

# Implement a function called display_info() which prints the name of the company
# and if the user also passes an argument named price , it prints the price.

def display_info(company, **kwargs):
    print(f'Company name: {company}')

    if 'price' in kwargs:
        print(f"Price: {kwargs['price']}")

display_info(company= 'Tesla', price= '100')

                # Company name: Tesla
                # Price: 100