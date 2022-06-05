# exercise 89: Convert an Integer to Its Ordinal Number

import random


def my_ordinal(n):
    if n < 1 or n > 12:
        return ''
    if n == 1:
        return 'first'
    elif n == 2:
        return 'second'
    elif n == 3:
        return 'third'
    elif n == 4:
        return 'fourth'
    elif n == 5:
        return 'fifth'
    elif n == 6:
        return 'sixth'
    elif n == 7:
        return 'seventh'
    elif n == 8:
        return 'eighth'
    elif n == 9:
        return 'ninth'
    elif n == 10:
        return 'tenth'
    elif n == 11:
        return 'eleventh'
    elif n == 12:
        return 'twelvfth'


def main():
    print('random ordinal between 1 and 12: ', end='')
    print(my_ordinal(random.randint(1, 12)))

    print()

    for i in range(1, 13):
        print(i, my_ordinal(i))


if __name__ == '__main__':
    main()
