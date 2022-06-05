secs_per_day = 86400
secs_per_hour = 3600
secs_per_minute = 60

seconds = int(input('insert seconds: '))

# even if it comes out with decimals, when printing using %02d decimals will be ignored
days = seconds / secs_per_day
# getting the exceeding seconds with modulo operator to get the additional seconds
seconds = seconds % secs_per_day
# same logic, now seconds are updated with exceeding seconds. They get divided by 3600, namely seconds in an hour
hours = seconds / secs_per_hour
seconds = seconds % secs_per_hour

minutes = seconds / secs_per_minute
seconds = seconds % secs_per_minute

print("%d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
