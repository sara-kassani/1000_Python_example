# exercise 74: Square Root

from math import sqrt

x = float(input('enter x: '))
square_root = sqrt(x)
print('square root of %.2f is' % (x), square_root)

print('implementation: ')
# the guess is initialized to x / 2 (but it does not really change much)
guess = x / 2

while abs(guess ** 2 - x) > 10 ** -12:
    guess = (guess + x / guess) / 2
    print(guess)

print(guess, '--> correct square root')

# note: using equality between guess and square_root as condition would lead to risk of infinite loop
