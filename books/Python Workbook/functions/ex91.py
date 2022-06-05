# exercise 91: Gregorian Date to Ordinal Date

# first thing to do is understanding if the year has 365 or 366 days
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# second thing is to get the total days within a month of a specific year
def days_in_month(month, year):
    days = 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        if is_leap(year):
            days = 29
        else:
            days = 28
    elif month < 1 or month > 12:
        raise ValueError('month must be between 1 and 12')
    return days


def greg_to_ord_date(day, month, year):
    ordinal = 0
    for m in range(1, month):
        ordinal += days_in_month(m, year)

    if day > days_in_month(month, year) or day < 1:
        raise ValueError('the entered day is not valid: it is outside that month\'s range of days')
    else:
        ordinal += day

    return ordinal


def main():
    day = int(input('enter day of the month as integer: '))
    month = int(input('enter month of the year as integer: '))
    year = int(input('enter year: '))

    print('it was day {} of {}'.format(greg_to_ord_date(day, month, year), year))


if __name__ == '__main__':
    main()










