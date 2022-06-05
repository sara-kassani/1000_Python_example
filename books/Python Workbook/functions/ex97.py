# exercise 97: Operator Precedence

def precedence(s):
    if s == '+' or s == '-':
        return 1
    elif s == '*' or s == '/':
        return 2
    elif s == '^':
        return 3
    else:
        return 'error, the input is not an operator'


def main():
    operator = input('enter operator: ')
    print(precedence(operator))


if __name__ == '__main__':
    main()
