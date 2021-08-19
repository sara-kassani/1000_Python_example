"""
complex if statement with boolean operators
"""
def main():
    age = 16
    name = 'Foo'

    if 0 < age and age <= 18:
        print("Age is between 0 and 18.")
    else:
        print("Age is not between 0 and 18.")


    if age < 18 or 65 < age:
        print('Young or old')
    else:
        print('Working age')


    if age < 18 and not name == 'Foo':
        print("True")
    else:
        print("False")



if __name__ == '__main__':
    main()