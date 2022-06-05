# exercise 58: Is It a Leap Year?

year = int(input('enter year: '))

if year % 400 == 0:
    res = 'leap'
elif year % 100 == 0:
    res = 'not leap'
elif year % 4 == 0:
    res = 'leap'
else:
    res = 'not leap'

print('year %d: %s year' % (year, res))


""" alternative:
at each if statement I might write isLeapYear = True or isLeapYear = False and then
use a final if-else printing alternative the one or the other text
"""
