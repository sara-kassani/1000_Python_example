# exercise 15: Distance Units

feet = float(input('insert feet: '))
inches = feet * 12
yards = feet * 0.3333
miles = yards * 0.000568
""" or
yards = feet / 3
miles = feet / 5280
"""

print('%.2f feet equal %.2f inches, %.5f yards, %.5f miles' % (feet, inches, yards, miles))
