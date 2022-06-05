# exercise 18: Volume of a Cylinder

import math


r = int(input('here is the radius: '))
height = int(input('here is the height in cm: '))
area = math.pi * r**2
volume = area * height
print('the cylinder has a volume of %.1f cm' % volume)
