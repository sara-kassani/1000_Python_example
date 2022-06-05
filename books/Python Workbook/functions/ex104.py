# exercise 104: Hexadecimal and Decimal Digits

def hex2int(hexa):

    if hexa.isdigit():  # checking if it is a number
        if 0 <= int(hexa) <= 9:
            integer = int(hexa)
            return integer

    hexa = hexa.upper()
    if hexa == 'A':
        integer = 10
    elif hexa == 'B':
        integer = 11
    elif hexa == 'C':
        integer = 12
    elif hexa == 'D':
        integer = 13
    elif hexa == 'E':
        integer = 14
    elif hexa == 'F':
        integer = 15
    else:
        return "that's not a hexadecimal"

    return integer


def int2hex(integer):
    if 0 <= integer <= 9:
        hexa = integer
        return hexa
    elif 10 <= integer <= 15:
        if integer == 10:
            hexa = 'A'
        elif integer == 11:
            hexa = 'B'
        elif integer == 12:
            hexa = 'C'
        elif integer == 13:
            hexa = 'D'
        elif integer == 14:
            hexa = 'E'
        else:
            hexa = 'F'
        return hexa
    else:
        return "No hexadecimal corresponding to that integer"


if __name__ == "__main__":
    h = input('enter hexadecimal: ')
    print(hex2int(h))
    print()
    i = int(input('enter integer: '))
    print(int2hex(i))
