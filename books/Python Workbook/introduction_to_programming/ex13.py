# exercise 13: Making Change

cents = int(input('resto da dare in centesimi: '))

# each coin's value in cents
penny = 1
dime = 10
quarter = 25
nickel = 50
loonie = 100
toonie = 200

# start determining how many (eventual) toonies I have to use
# using floor division allows to see if the result is 0.something, in that case I will not use the coin
# here dividing by 200, namely the value of a toonie in cents
print("", cents // toonie, "toonies")
# updating the amount to give in cents, by using modulo operator
# note that if to the left of % I have a smaller number than to the right, the remainder is the value to the left
cents = cents % toonie

print("", cents // loonie, "loonies")
cents = cents % loonie

print("", cents // nickel, "nickels")
cents = cents % nickel

print("", cents // quarter, "quarters")
cents = cents % quarter

print("", cents // dime, "dimes")
cents = cents % dime

print("", cents // penny, "pennies")
cents = cents % penny

"""
explanation: case of 57 cents as a change to give:
- in the first print the result will be 0 toonies: 50 // 200 = 0
and the value in cents will be updated by dividing through modulo operator, but the
remainder will be 57 cents itself because 57 % 200 = 57.
- in the second print the same thing applies: 57 // 100 = 0 and 57 % 100 = 57.
- in the third print 57 // 50 = 1, thus I use 1 nickel and update the valuein cents,
but this time 57 % 50 = 7, thus thera are 7 remaining cents to give.
- in the fourth print 7 // 25 = 0 and 7 % 25 = 7, nothing changes, 0 quarters used.
- in the fifth print 7 // 10 = 0 and 7 % 10 = 7, nothing changes again.
- in the sixth and last print, 7 // 1 = 7, thus I use 7 pennies
and update the value in cents, by doing t % 1 = 0 (because 1 goes into the 7 exatcly 7 times without remainder.
No more change to give.
"""

