# exercise 179: Recursive Square Root

from math import sqrt


def square_root(n, guess=1.0):
    if 10**-12 >= abs(guess**2 - n):
        return guess
    else:
        guess = (guess + n / guess) / 2
        return square_root(n, guess)


def main():
    number = float(input('enter a number: '))
    print('its official square root is', sqrt(number))
    print('my estimated square root is', square_root(number, number / 2))


if __name__ == '__main__':
    main()

# note: the first condition in the function is the same as abs(guess**2 - n) <= 10**-12
