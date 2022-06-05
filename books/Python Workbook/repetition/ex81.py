# exercise 81: Binary to Decimal

"""
conversion logic:
1010 is 10 namely 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 2^3 + 2 = 10
10010 is 18 namely 2^4 + 2
11011 is 27 ---> note that if the first value to the right is 1 it will be 1*2^0 = 1
"""

binary = input('enter binary number: ')
decimal = 0
# since I start reading from left in the string, I start raising to the highest power
power = len(binary) - 1
# using the index to loop on each binary number
i = 0
# loop continues until getting to power zero nanmely the last number to the right
while power >= 0:
    # using the conversion rule at each iteration
    decimal += int(binary[i]) * 2 ** power
    # reducing power when moving to the right
    power -= 1
    # increasing index to iterate towards right

print('the decimal of %s is %d' % (binary, decimal))
