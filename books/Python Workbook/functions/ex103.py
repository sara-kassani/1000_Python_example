# exercise 103: Random Good Password

from functions.ex100 import random_pwd
from functions.ex102 import checkPassword


def main():
    attempts = 0
    while True:
        mypwd = random_pwd()
        attempts += 1
        print('attempt number', attempts, '-->', mypwd)
        if checkPassword(mypwd):
            return print('The password was saved!')


if __name__ == '__main__':
    main()
