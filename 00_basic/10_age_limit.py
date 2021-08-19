'''
Exercise: Age limit
Ask the user what is their age
If it is above 18, tell them they can legaly drink alcohol.
If it is above 21, tell them they can also legally drink in the USA
'''

def main():
    age = float(input('Enter your age: '))
    country = input('Enter the name of country: ')

    if 21 <= age:
        print( 'You can drink')
    elif 18 <= age:
        print('You can drink (But not in the USA)')
    else:
        print('You cannot legally drink')

if __name__ == '__main__':
    main()