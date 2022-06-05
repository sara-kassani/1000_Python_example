# exercise 19: Free Fall

import math


distance = float(input('meters the object drops from: '))
acceleration = 9.8
initial_speed = 0
final_speed = math.sqrt(initial_speed + 2 * acceleration * distance)
print('the final speed of the object when it hits the ground is %.2f m/s' % final_speed)
