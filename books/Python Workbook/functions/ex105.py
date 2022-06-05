# exercise 105: Arbitrary Base Conversions

def dec2n(num, b):
    """
    the function converts a decimal into a number of base b
    parameter num is the decimal to convert
    parameter b is the base to convert the decimal to
    r is the remainder
    new remainders always go to the left side of the result
    q is the quotient
    """
    b = int(b)
    res = ''
    r = num % b
    res = str(r) + res
    q = num // b

    # repeating the same operations (considering q as the num), until q equals zero
    while q > 0:
        r = q % b
        res = str(r) + res
        q = q // b

    return res


def n2dec(num, b):
    """
    the function converts a number from base b to a decimal
    parameter num is the number with base b that has to be converted into a number with base 10
    index is used to loop each digit from right to left
    i is the increasing power from 0 to length of num minus 1
    """
    b = int(b)
    decimal = 0
    index = len(num) - 1

    for i in range(len(num)):
        digit = int(num[index])
        decimal += digit * (b ** i)
        index -= 1

    return decimal


def main():
    # converting a number from an arbitrary base into a decimal
    from_base = input('enter base to convert from: ')
    from_num = input('enter number to convert: ')
    dec = n2dec(from_num, from_base)
    print('{} in base {} corresponds to decimal {}'.format(from_num, from_base, dec))

    # converting the previous decimal into a number with arbitrary base
    to_base = input('enter a base to convert to: ')
    dec_converted = dec2n(dec, to_base)
    print('decimal {} corresponds to {} in base {}'.format(dec, dec_converted, to_base))


if __name__ == '__main__':
    main()


# to add: possibility to use hexadecimal letters
