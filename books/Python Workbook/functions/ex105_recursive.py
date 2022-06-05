# exercise 105: Arbitrary Base Conversions

def dec2n(num, b):
    res = ''
    # r is the remainder
    r = num % b
    # new remainders go to the left side of the result
    res = str(r) + res

    # q is initialized as a quotient
    # if it is more than zero, the function keeps calling itself considering q as the num
    # when calling itself, the previous result string is kept to the right side
    q = num // b
    if q > 0:
        res = dec2n(q, b) + res

    # the recursion stops when q equals zero
    return res


def main():
    decimal_to_convert = int(input('enter decimal to convert: '))
    base_to_convert_to = int(input('enter base to convert to: '))
    print(dec2n(decimal_to_convert, base_to_convert_to))


if __name__ == '__main__':
    main()
