# exercise 12: Distance Between Two Point on Earth

import math


t1 = float(input('enter latitude 1: '))
t2 = float(input('enter latitude 2: '))
g1 = float(input('enter longitude 1: '))
g2 = float(input('enter longitude 2: '))

# converting into radians

t1 = math.radians(t1)
t2 = math.radians(t2)
g1 = math.radians(g1)
g2 = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print('the distance between the two points on Earth is %.4f kilometers' % distance)
