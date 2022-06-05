# exercise 101: Random License Plate

from random import randint

A_ord = 65
Z_ord = 90
zero_ord = 48
nine_ord = 57


def random_license_plate():
    type_of_license = randint(1, 2)
    license_plate = ''

    if type_of_license == 1:  # old license
        type_of_license = 'older'
        for i in range(3):
            random_letter = randint(A_ord, Z_ord)
            license_plate += chr(random_letter)
        for i in range(3):
            random_number = randint(zero_ord, nine_ord)
            license_plate += chr(random_number)
        return '%s (%s)' % (license_plate, type_of_license)

    if type_of_license == 2:  # new license
        type_of_license = 'newer'
        for i in range(4):
            random_number = randint(zero_ord, nine_ord)
            license_plate += chr(random_number)
        for i in range(3):
            random_letter = randint(A_ord, Z_ord)
            license_plate += chr(random_letter)
        return '%s (%s)' % (license_plate, type_of_license)


if __name__ == '__main__':
    print(random_license_plate())
