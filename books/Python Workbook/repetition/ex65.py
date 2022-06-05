# exercise 65: Temperature Conversion Table

for C in range(0, 110, 10):
    F = C * (9 / 5) + 32
    if C == 0:
        print('°C      °F   ')
        print('------------')
        print("°%d      °%d" % (C, F))
    elif C >= 100:
        print("°%d    °%d" % (C, F))
    else:
        print("°%d     °%d" % (C, F))
