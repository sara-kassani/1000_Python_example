# exercise 22: Area of a Triangle (Again)

import math


s1 = int(input('insert length of side 1: '))
s2 = int(input('insert length of side 2: '))
s3 = int(input('insert length of side 3: '))

s = ((s1 + s2 + s3) / 2)

# Erone formula
area_triangle = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

print('area: %.2f' % area_triangle)

