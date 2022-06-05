# exercise 107: Reduce a Fraction to Lowest Terms

def reduceFraction(numerator, denominator):
    print("I am going to reduce %d / %d" % (numerator, denominator))
    # GCD cannot be higher than the lowest between numerator and denominator
    d = min(numerator, denominator)
    # reducing d until both numerator and denominator are both divisible by d
    while numerator % d != 0 or denominator % d != 0:
        d -= 1

    numerator_reduced = numerator / d
    denominator_reduced = denominator / d
    # checking if one of the two terms of the fraction has been actually reduced
    if numerator_reduced != numerator:
        return ">>> %d / %d" % (numerator_reduced, denominator_reduced)
    # if even one only of the two terms was not reducet, it means the fraction is already reduced
    else:
        return "the fraction cannot be reduced"


if __name__ == '__main__':
    num = int(input('enter numerator: '))
    den = int(input('enter denominator: '))
    print(reduceFraction(num, den))
