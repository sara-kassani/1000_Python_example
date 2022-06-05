# exercise 114: Negatives, Zeroes and Positives

numbers = []
n = int(input('enter integer (blank to quit): '))

while n != '':
    n = int(n)
    numbers.append(n)
    n = input('enter integer (blank to quit): ')

negatives = []
zeroes = []
positives = []

# looping each element of the created list and pushing it into one of the three list based on its sign
for number in numbers:
    if number < 0:
        negatives.append(number)
    elif number > 0:
        positives.append(number)
    else:
        zeroes.append(number)

# joining the three lists together and making them becoming one sorted list only
new_numbers = negatives + zeroes + positives

# lastly I print each element of the resulting list
for number in new_numbers:
    print(number)

# note: the creation of the initial list can be avoided
