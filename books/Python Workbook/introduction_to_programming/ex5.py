# exercise 5: Bottle Deposits

smaller_deposit = 0.10
bigger_deposit = 0.25

less = int(input('how many 1 liter bottles do you have? '))
more = int(input('how many more than 1 liter bottles do you have? '))

total_refund = less*smaller_deposit + more*bigger_deposit
print('You are going to get $%.2f back' % total_refund)