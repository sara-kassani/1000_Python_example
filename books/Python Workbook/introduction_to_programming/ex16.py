# exercise 16: Area and Volume

import math


r = int(input('indicate radius: '))
area_circle = math.pi * r**2
volume_sphere = (4 / 3) * math.pi * r**3
print('the area of a circle with radius %d is %.2f' % (r, area_circle))
print('the volume of a sphere with radius %d is %.2f' % (r, volume_sphere))
