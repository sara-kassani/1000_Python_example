# exercise 52: Letter Grade to Grade Points

grade = input("enter letter grade: ")
points = ""

if grade == "F":
    points = 0
elif grade == "D":
    points = 1
elif grade == "D+":
    points = 1.3
elif grade == "C-":
    points = 1.7
elif grade == "C":
    points = 2
elif grade == "C+":
    points = 2.3
elif grade == "B-":
    points = 2.7
elif grade == "B":
    points = 3
elif grade == "B+":
    points = 3.3
elif grade == "A-":
    points = 3.7
elif grade == "A" or grade == "A+":
    points = 4


if points != "":
    print("a letter grade of {} corresponds to {} points".format(grade, points))
# if points was not assigned a value, it means input was not valid
else:
    print("please enter a valid letter grade. Remember to use uppercase.")