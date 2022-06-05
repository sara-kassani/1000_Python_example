# exercise 156: Sum a Collection of Numbers

value = input('enter an integer or a decimal: ')

sum = 0

while value != '':
    # if the code below the try encounters a ValueError, the code below the except will be executed
    try:
        # attempting to convert input in a decimal number
        num = float(value)
        sum += num
        print('%.1f' % sum)
        value = input('enter an integer or a decimal: ')

    except ValueError:
        print('that\'s not a number')
        value = input('enter an integer or a decimal: ')

print('final sum is %.1f' % sum)
