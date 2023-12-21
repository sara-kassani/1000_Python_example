"""
Implement a function called stick( ) that takes any number of bare arguments and return an object of type
str being a concatenation of all arguments of type str passed to the function with the '#' sign
"""
def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]

    result="#".join(args)
    return result

print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(False, 'time', True, 'workout', [], 'gym')


"""
sport#summer

False time True workout [] gym

"""