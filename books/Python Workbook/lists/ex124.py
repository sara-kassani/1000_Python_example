# exercise 124: Line of Best Fit

all_x = []
all_y = []
all_xy = []
all_xsquare = []

x = input('enter x: ')
y = input('enter y: ')
n = 0

while True:
    n += 1
    x = float(x)
    y = float(y)
    all_x.append(x)
    all_y.append(y)
    xy = x * y
    xsquare = x ** 2
    all_xy.append(xy)
    all_xsquare.append(xsquare)
    x = input('enter x (blank to quit): ')
    # the condition which stops the loop is a blank line for x
    if x == '':
        break
    y = input('enter y: ')

sum_x = sum(all_x)
sum_y = sum(all_y)
sum_xy = sum(all_xy)
sum_xsquare = sum(all_xsquare)
avg_x = sum_x / n
avg_y = sum_y / n

m_numerator = sum_xy - (sum_x * sum_y) / n
m_denominator = sum_xsquare - (sum_x ** 2) / n
m = m_numerator / m_denominator
b = avg_y - m * avg_x

# printing y = mx + b after substituting the m and b values that were found
print('y = %.2fx + %.2f' % (m, b))

""" tests
print('sum of x is %d'%sum_x)
print('sum of y is %d'%sum_y)
print('sum of xy is %d'%sum_xy)
print('avg x is %.1f'%avg_x)
print('avg y is %.1f'%avg_y)
"""
