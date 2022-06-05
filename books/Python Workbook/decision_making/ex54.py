# exercise 54: Assessing Employees

rating = float(input("enter rating: "))

if rating == 0:
    performance = "unacceptable"
    amount = 0
elif rating == 0.4:
    performance = "acceptable"
    amount = 2400 * rating
elif rating >= 0.6:
    performance = "meritorious"
    amount = 2400 * rating
else:
    performance = ""
    print('invalid rating')

if performance:
    print('performance: %s \nraise: $%.2f' % (performance, amount))
