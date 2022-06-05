# exercise 52: Letter Grade to Grade Points

def lett_to_point(grade):
    try:
        grade = grade.upper()
    except:
        raise ValueError('please enter a letter grade')

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
    else:
        raise ValueError('please enter a letter grade between A and F (+ or - can be included)')

    return points


def main():
    mygrade = input('enter a letter grade: ')
    print('{} corresponds to {} points'.format(mygrade.upper(), lett_to_point(mygrade)))


if __name__ == '__main__':
    main()
