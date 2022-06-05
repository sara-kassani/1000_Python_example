# exercise 119: Below and Above Average

numbers = []
n = input('enter a number (blank to quit): ')
acc = 0

while n != '':
    n = int(n)
    acc += n
    numbers.append(n)
    n = input('enter a number (blank to quit): ')

avg = acc / len(numbers)

below_avg = []
above_avg = []
avg_values = []

for i in numbers:
    if i < avg:
        below_avg.append(i)
    elif i > avg:
        above_avg.append(i)
    else:
        avg_values.append(i)

print(numbers)
print('average value: %.1f' % avg)
print('below average values >>> {}'.format(below_avg))
if avg_values:  # if list was empty the condition would not apply
    print('average values >>> {}'.format(avg_values))
print('above average >>> {}'.format(above_avg))

