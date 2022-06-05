# exercise 177: Roman Numerals

"""
M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1
when all numerals are in descendent order:
XVII = 10+5+2 = 17
when not all numerals are in descendent order:
XIV = 10+(5-1) = 14
"""


def roman_value(s):
    if s == 'M':
        return 1000
    elif s == 'D':
        return 500
    elif s == 'C':
        return 100
    elif s == 'L':
        return 50
    elif s == 'X':
        return 10
    elif s == 'V':
        return 5
    elif s == 'I':
        return 1
    else:
        raise ValueError('not a valid roman numeral')


def roman_to_integer(roman):
    # BASE CASE
    # if there are no numerral left, I add zero to the sum and recursion ends
    if roman == '':
        return 0

    # if there is one numeral left, I add its value to the sum
    if len(roman) == 1:
        return roman_value(roman)

    # if there are still two numerals, I convert them in integer in order to compare them
    preceding = roman_value(roman[0])
    following = roman_value(roman[1])

    # if the preceding is a higher value, I add it to the sum and call the function again from the following
    if preceding >= following:
        return preceding + roman_to_integer(roman[1:])
    # if the preceding is lower, I subtract it from the following and add the subtraction to the sum
    # then I call the function again but from the numeral which comes next to the following
    elif preceding < following:
        return (following - preceding) + roman_to_integer(roman[2:])


if __name__ == '__main__':
    roman_number = input('enter a roman number: ')
    print(roman_to_integer(roman_number))


