# exercise 85: Compute the Hypotenuse

import math


def find_hypo(l1, l2):
    h = math.sqrt(l1 ** 2 + l2 ** 2)
    return h


def main():
    side1 = float(input('enter length of side 1: '))
    side2 = float(input('enter length of side 2: '))

    hypotenuse = find_hypo(side1, side2)
    print('the hypotenuse of a right triangle with sides %.1f and %.1f is %.1f' % (side1, side2, hypotenuse))


if __name__ == '__main__':
    main()
