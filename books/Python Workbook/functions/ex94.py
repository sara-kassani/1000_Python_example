# exercise 94: Is It a Valid Triangle?

def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True


def triangle_details(a, b, c):
    sum_bc = b + c
    sum_ac = a + c
    sum_ab = a + b

    if is_triangle(a, b, c):
        print("that's a triangle because:")
        print("a = %d < b + c = %d" % (a, sum_bc))
        print("b = %d < a + c = %d" % (b, sum_ac))
        print("c = %d < a + b = %d" % (c, sum_ab))
    else:
        print("that's not a triangle because:")
        if a >= sum_bc:
            print('a = %d >= b + c = %d' % (a, sum_bc))
        elif b >= sum_ac:
            print('b = %d >= a + c = %d' % (b, sum_ac))
        elif c >= sum_ab:
            print('c = %d >= a + b = %d' % (c, sum_ab))

def main():
    len1 = int(input('enter length: '))
    len2 = int(input('enter length: '))
    len3 = int(input('enter length: '))
    triangle_details(len1, len2, len3)


if __name__ == '__main__':
    main()
