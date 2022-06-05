# exercise 14: Height Units

feet = int(input('insert number of feet: '))
inches = int(input('insert number of inches: '))
a_foot_in_inches = 12
a_inch_in_cm = 2.54
tot_centimeters = feet * a_foot_in_inches * a_inch_in_cm + inches * a_inch_in_cm
print('%.1f cm' % tot_centimeters)
