# exercise 4: Area of a Field

length = float(input('enter the length of the field: '))
width = float(input('enter the width of the field: '))
area_square_feet = length * width
area_acres = area_square_feet / 43560
print('the field is {} acres'.format(area_acres))