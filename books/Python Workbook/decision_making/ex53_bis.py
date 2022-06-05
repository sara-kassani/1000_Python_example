# exercise 53: Grade Points to Letter Grade

def point_to_lett(points):
    try:
        points = float(points)
    except:
        raise ValueError('please enter a digit')

    if points >= 4:
        grade = "A+"
    elif points >= 3.86:
        grade = "A"
    elif points >= 3.5:
        grade = "A-"
    elif points >= 3.16:
        grade = "B+"
    elif points >= 2.86:
        grade = "B"
    elif points >= 2.5:
        grade = "B-"
    elif points >= 2.16:
        grade = "C+"
    elif points >= 1.86:
        grade = "C"
    elif points >= 1.5:
        grade = "C-"
    elif points >= 1.16:
        grade = "D+"
    elif points >= 0.86:
        grade = "D"
    elif 0 <= points < 0.86:
        grade = "F"
    else:
        raise ValueError('negative digits are not allowed')

    return grade


def main():
    mygrade = input('enter a point grade: ')
    print('{} corresponds to {}'.format(mygrade, point_to_lett(mygrade)))


if __name__ == '__main__':
    main()
