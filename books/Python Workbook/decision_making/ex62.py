# exercise 62: Roulette Payouts

import random

# storing random value between 0 and 37, considering 37 as my 00
number = random.randrange(0, 38)

if number == 00 or number == 37:
    if number == 0:
        print('the spin resulted in 0')
        print('pay 0')
    # if random generation generated 37, I consider it as my 00
    elif number == 37:
        print('the spin resulted in 00')
        print('pay 00')
# if any number between 1 and 36 was generated, I print it as it is
else:
    print('the spin resulted in %d' % number)

""" Alternative (input): 
# start by asking input as a string in order to differentiete between 0 and 00
# thus, first thing is printing the number as a string
print('the spin resulted in %s' % number)

# then I can differentiate 0 and 00 because they were entered as strings
if number == '00' or number == '0':
    if number == 0:
        print('pay 0')
    elif number == 00:
        print('pay 00')
# otherwise it means I can consider the number as integer
else:
    number = int(number)
"""

if 1 <= number <= 36:
    # printing for sure the prize of the number which is different from 0 and 00
    print('Pay %d' % number)
    if number == 1 or number == 3 or number == 5 or number == 7 or number == 9 or number == 12 \
        or number == 14 or number == 16 or number == 18 or number == 19 or number == 21 or \
            number == 23 or number == 25 or number == 27 or number == 30 or number == 32 \
                or number == 34 or number == 36:
                print('Pay Red')
    else:
        print('Pay Black')
    if number % 2 == 0:
        print('Pay Even')
    else:
        print('Pay Odd')
    if number <= 18:
        print('Pay 1 to 18')
    else:
        print('Pay 19 to 36')
