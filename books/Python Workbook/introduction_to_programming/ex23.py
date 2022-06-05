# exercise 23: Area of a Regular Polygon

import math


s = float(input('enter length of sides: '))
n = int(input('enter number of sides: '))
area_polygon = (n * s**2) / (4 * math.tan(math.pi / n))
print('the area of a polygon with %d sides of length %d is %.2f' % (n, s, area_polygon))
