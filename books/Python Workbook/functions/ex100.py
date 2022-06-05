# exercise 100: Random Password

import random


def random_pwd():
    pwd = ''
    length = random.randint(7, 10)
    for i in range(length):
        chr_code = random.randint(33, 126)
        pwd += chr(chr_code)
    return pwd


if __name__ == '__main__':
    print(random_pwd())
