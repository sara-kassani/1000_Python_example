# exercise 175: Recursive Decimal to Binary

def decimal_to_binary(n):
    res = ''
    if n == 0:
        return 0
    if n == 1:
        res = str(1) + res
        return res
    elif n > 0 and isinstance(n, int):
        r = n % 2
        res = str(r) + res
        n = n // 2
        # I add the return of the recursive function to the left side of the previous res
        return decimal_to_binary(n) + res
    else:
        return 'error: the number must be a positive integer'


def main():
    try:
        number = int(input('enter a positive integer to convert to binary: '))
        print(decimal_to_binary(number))
    except:
        print('please enter an integer')


if __name__ == '__main__':
    main()
