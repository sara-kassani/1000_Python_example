# Conditionals: elif

def main():
    a = input('First number: ')
    b = input ('Second number')

    if a == b:
        print('Equal')
    elif int(a) < int(b):
        print(a + ' is smaller than ' + b)
    else:
        print(a + ' is greater than ' + b)

if __name__ == '__main__':
    main()