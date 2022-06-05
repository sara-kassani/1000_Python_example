# exercise 24: Units of Time

d = int(input('days: '))
h = int(input('hours: '))
m = int(input('minutes: '))
s = int(input('seconds: '))

tot_seconds = d * 86400 + h * 3600 + m * 60 + s
print('%d days, %d hours, %d minutes and %d seconds correspond in total to %d seconds' % (d, h, m, s, tot_seconds))
