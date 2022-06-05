# exercise 66: No More Pennies

PENNIES_PER_NICKEL = 5
NICKEL = 0.05

total = 0.00

line = input('enter price of the item: ')

while line != '':
    total = total + float(line)
    line = input('enter price of the item: ')

print('the exact payable amount is %.02f' % total)

# computing the number of pennies that would be left if total was paid only with nickels
rounding_indicator = total * 100 % PENNIES_PER_NICKEL

# I distinguish if the remainder is less or more than 2.5
if rounding_indicator < PENNIES_PER_NICKEL / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + NICKEL - rounding_indicator / 100

print('amount due is %.02f' % cash_total)
