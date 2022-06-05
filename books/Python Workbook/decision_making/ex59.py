# exercise 59: Next Day

# formatted as yyyy-mm-dd
date = input('enter date: ')
# extracting values from the string yyyy-mm-dd, treating them as integers from now on
year = int(date[:4])
month = int(date[5:7])
day = int(date[8:])

# error checking
if month < 1 or month > 12:
    print('enter a valid month')
    exit()
if day < 1 or day > 31:
    print('enter a valid day')
    exit()

# the only case when year changes
if day == 31 and month == 12:
    year += 1
    month -= 11
    day -= 30
# case when month changes for sure: day 31
elif day == 31:
    month += 1
    day -= 30
# when day is 30, I make distinctions based on month
elif day == 30:
    if month == 4 or month == 6 or month == 9 or month == 11:
        month += 1
        day -= 29
    else:
        day += 1
# when having 29 february, month and day will change for sure
elif day == 29 and month == 2:
    month += 1
    day -= 28
# when having 28 february, I have to check if it is a leap year or not
elif day == 28 and month == 2:
    # LEAP
    if year % 400 == 0:
        day += 1
    # NOT LEAP
    elif year % 100 == 0:
        month += 1
        day -= 27
    # LEAP
    elif year % 4 == 0:
        day += 1
    # NOT LEAP
    else:
        month += 1
        day -= 27
# in any other case only day will change
else:
    day += 1

# writing %02d makes sure the number will have at least 2 digits
# thus, for number lower than 10, there will be a leading zero
print("%d-%02d-%02d"%(year, month, day))
