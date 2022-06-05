# exercise 71: Approximate

# initial value given to pi
pi = 3
a = 2
b = 3
c = 4

# i will be approximated 15 times
for i in range(1, 15):
    # all odd iterations
    if i % 2 != 0:
        pi += 4 / (a*b*c)
    # all even iterations
    else:
        pi -= 4 / (a*b*c)
    a += 2
    b += 2
    c += 2




print(pi)