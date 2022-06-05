# exercise 66: No More Pennies

price = 0
tot_cost = 0

price = input('enter price: ')

while price != '':
    # setting that prices can have max two decimals, otherwise input is not valid
    # if decimals are present, price gets divided in two elements, where the second is the string with decimals
    # in other words, price will be considered if it is integer or decimal but with maximum two decimals
    if '.' not in price or len(price.split('.')[1]) <= 2:
        tot_cost += float(price)
        price = input('enter price: ')
    else:
        print('last input was not valid: please rewrite.')
        price = input('enter price: ')

# computing the total number of pennies from total cost
tot_pennies = tot_cost * 100

# computing the remainder of the number of pennies divided by 5
# namely the number of pennies that will remain if I payed only with nickels
remainder = tot_pennies % 5

print('tot cost: %.2f' % tot_cost)
# print('tot pennies: %.2f'%tot_pennies)
# print('remainder: ',round(remainder))

# using round to approximate the remainder to the closest integer
if round(remainder) == 4:
    tot_pennies += 1
if round(remainder) == 3:
    tot_pennies += 2
if round(remainder) == 2:
    tot_pennies -= 2
if round(remainder) == 1:
    tot_pennies -= 1

# reporting the total cost expressed in pennies in a readable cost, dividing again by 100
tot_cost = tot_pennies / 100

print('final cost: %.2f' % tot_cost)
