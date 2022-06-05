# exercise 10: Arithmetic

from math import log10

a = int(input('insert value for a: '))
b = int(input('insert value for b: '))
sum = a + b
difference = a - b
product = a * b
quotient = a / b
logarithm = log10(a)
remainder = a % b
power = a**b

print('given two numbers a = %d and b = %d' % (a, b), '\nsum is %d \ndifference a minus b is %d\
    \nproduct is %d \nquotient a divided by b is %.1f \nlogarithm of a is %.2f \nremainder of a divided by b is %d\
    \na to the b is %d' % (sum, difference, product, quotient, logarithm, remainder, power))