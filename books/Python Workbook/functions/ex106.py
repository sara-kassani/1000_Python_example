# exercise 106: Days In a Month

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(month, year):
    if month < 1 or month > 12 or len(str(year)) != 4:  # error checking
        return 'the input is not valid'

    if month == 11 or month == 4 \
            or month == 6 or month == 9:
        num_of_days = 30
    elif month == 2:
        # condition depends on the return of the function which says if a year is leap or not
        if isLeap(year):
            num_of_days = 29
        else:
            num_of_days = 28
    else:
        num_of_days = 31
    return num_of_days


if __name__ == "__main__":
    month = int(input('enter a month as an integer: '))
    year = int(input('enter a year: '))
    print(daysInMonth(month, year))

