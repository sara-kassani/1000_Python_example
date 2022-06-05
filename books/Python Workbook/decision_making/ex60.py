# exercise 60: What Day of the Week is January 1?

import datetime

year = int(input('enter a year and you will get its January 1 day: '))

# the following formula finds the day of the week (as integer 0-6) of January 1st
weekday = (year + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)) % 7

if weekday == 0:
    res = 'sunday'
elif weekday == 1:
    res = 'monday'
elif weekday == 2:
    res = 'tuesday'
elif weekday == 3:
    res = 'wednesday'
elif weekday == 4:
    res = 'thursday'
elif weekday == 5:
    res = 'friday'
elif weekday == 6:
    res = 'saturday'

# extracting today's year in order to differentiate the tense of the output string
now = datetime.datetime.now()
current_year = now.year

if year > current_year:
    print('January 1st of %d will be a %s'%(year, res))
else:
    print('January 1st of %d was a %s'%(year, res))
