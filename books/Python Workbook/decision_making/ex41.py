# exercise 41: Classifying Triangles

side1 = int(input("enter length of side 1: "))
side2 = int(input("enter length of side 2: "))
side3 = int(input("enter length of side 3: "))

if side1 == side2 and side2 == side3:
    name = "equilateral"
else:
    if side1 == side2 or side2 == side3 or side1 == side3:
        name = "isosceles"
    else:
        name = "scalene"

print("that's a {} triangle".format(name))
