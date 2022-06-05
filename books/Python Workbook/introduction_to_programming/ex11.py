# exercise 11: Fuel Efficiency

MPG = float(input('insert miles per gallon: '))

a_gallon_in_L = 3.785
a_mile_in_Km = 1.61

# e.g. 25 miles per gallon equal 40.25 Km per 3.785 L
# consequently, in order to find L/100Km I will have to find x in --> 40.25 : 3.785 = 100 : x
# in other words I want to find the number of liters needed to do 100 Km,
# given that with 3.785L (1 gallon) I do 40.25 Km (25 miles)
# to sum up the formula, it is L/100Km = (gallon in L * 100) / (MPG * mile in Km)

L_per_100Km = (a_gallon_in_L * 100) / (MPG*a_mile_in_Km)

print('%.2f miles per gallon are equal to %.2f liters per 100 Km' % (MPG, L_per_100Km))

# ALTERNATIVE
"""
formula_Lper100Km = 235.21 / MPG
print('%.2f' % formula_Lper100Km)
"""