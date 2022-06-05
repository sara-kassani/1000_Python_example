# exercise 53: Grade Points to Letter Grade

points = float(input('enter grade in points: '))

if points >= 4:
    grade = "A+"
elif points > 3.85:
    grade = "A"
elif points > 3.5:
    grade = "A-"
elif points > 3.15:
    grade = "B+"
elif points > 2.85:
    grade = "B"
elif points > 2.5:
    grade = "B-"
elif points > 2.15:
    grade = "C+"
elif points > 1.85:
    grade = "C"
elif points > 1.5:
    grade = "C-"
elif points > 1.15:
    grade = "D+"
elif points > 0.5:
    grade = "D"
elif 0 <= points <= 0.5:
    grade = "F"
else:
    grade = None

if grade:
    print("%g is %s" % (points, grade))
else:
    print('point grade is not valid')

