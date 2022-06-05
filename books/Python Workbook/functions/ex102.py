# exercise 102: Check a Password

def checkPassword(s):
    if len(s) < 8:
        return False

    uppers = 0
    lowers = 0
    numbers = 0
    for c in s:
        if c.isupper():
            uppers += 1
        if c.islower():
            lowers += 1
        if c.isdigit():
            numbers += 1

    if uppers > 0 and lowers > 0 and numbers > 0:
        return True
    else:
        return False


def main():
    mypwd = input('enter a password: ')
    if checkPassword(mypwd):
        print('password saved!')
    else:
        print("that's not a valid password")


if __name__ == '__main__':
    main()
