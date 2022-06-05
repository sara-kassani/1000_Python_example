# exercise 68: Compute a Grade Point Average

# points will be a cumulative value of all grade points
points = 0
# number of grades that will correspond to number of loops
n = 0
grade = input("enter letter grade: ")

# loops continues until a grade will be empty
while grade != "" and grade != " ":
    # counting the iterations, this number will be useful to compute average
    n += 1
    if grade == "F":
        points += 0
    elif grade == "D":
        points += 1
    elif grade == "D+":
        points += 1.3
    elif grade == "C-":
        points += 1.7
    elif grade == "C":
        points += 2
    elif grade == "C+":
        points += 2.3
    elif grade == "B-":
        points += 2.7
    elif grade == "B":
        points += 3
    elif grade == "B+":
        points += 3.3
    elif grade == "A-":
        points += 3.7
    elif grade == "A" or grade == "A+":
        points += 4
    # asking a new input at the end of each iteration
    grade = input("enter letter grade: ")

average = points / n

print("grade point average: %.1f" % average)
