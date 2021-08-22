"""
f-strings (formatted string literals)
"""


def main():
    name = "Foo Bar"
    age = 42.12
    pi = 3.1414592653589793
    r = 2

    print(f'The user {name} was born {age} years ago.')
    print(f'The user {name:10} was born {age} years ago.')
    print(f'The user {name:>10} was born {age} years ago.')
    print(f'The user {name:>10} was born {age:>10} years ago.')

    print(f"PI is '{pi:.3}'.")         # number of digits (defaults n = number)
    print(f"PI is '{pi:.3f}'.")        # number of digits after decimal points

    print(f"Area is {pi * r ** 2}")
    print(f"Area is {pi * r ** 2:.3f}")

    
if __name__ == '__main__':
    main()


