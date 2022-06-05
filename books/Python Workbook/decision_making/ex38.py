# exercise 38: Name That Shape

sides = int(input("enter the number of sides: "))

polygon = ""

if sides == 3:
    polygon = 'triangle'
elif sides == 4:
    polygon = "quadrilateral"
elif sides == 5:
    polygon = "pentagon"
elif sides == 6:
    polygon = "hexagon"
elif sides == 7:
    polygon = "heptagon"
elif sides == 8:
    polygon = "octagon"
elif sides == 9:
    polygon = "nonagon"
elif sides == 10:
    polygon = "decagon"

# if polygon was not assigned anything (empty) it means the number of sides is not valid
if polygon == "":
    print("error: enter a number of sides between 3 and 10")
else:
    print("It is a {}".format(polygon))




