# exercise 51: Roots of a Quadratic Function

import math


a = float(input("enter a value: "))
b = float(input("enter b value: "))
c = float(input("enter c value: "))

discriminant = (b**2) - (4 * a * c)


if discriminant < 0:
    print("the quadratic equation does not have any real roots")

elif discriminant == 0:
    result = (-b / (2 * a))
    print(result)
else:
    root1 = (- b - math.sqrt(discriminant)) / (2 * a)
    root2 = (- b + math.sqrt(discriminant)) / (2 * a)
    print("root 1 is %.2f and root 2 is %.2f" % (root1, root2))
