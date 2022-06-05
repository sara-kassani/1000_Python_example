# exercise 67: Compute the Perimeter of a Polygon

import math

x = int(input('enter x coordinate: '))
y = int(input('enter y coordinate: '))
# assigning the two inputs as the initial values for x and y
x_init = x
y_init = y
perimeter = 0

while True:
    # at each loop I assign the last two values to two variables x0 and y0 that are useful to compute new distance
    x0 = int(x)
    y0 = int(y)
    x = input('enter x coordinate: (blank to quit) ')
    # if x is not empty, then I ask the input of y to compute the new distance
    if x != '':
        y = input('enter y coordinate: ')
        x1 = int(x)
        y1 = int(y)
        distance = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        # at each loop I add to the perimeter the distance between new and old point
        perimeter += distance
    # if x input is empty instead
    else:
        # then I compute the distance from the last point to the initial point
        distance = math.sqrt((x0 - x_init) ** 2 + (y0 - y_init) ** 2)
        perimeter += distance
        # after the empty input the loop ends
        break

print('%.2f' % perimeter)
