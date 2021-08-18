# Exercise: calculator - argv

import sys
def main():
    if len(sys.argv) < 4:
        exit('Usage: ' + sys.argv[0] + 'OPERAND OPERATOR OPERAND')

    a = float(sys.argv([1]))
    b = float(sys.argv([3]))

    op = sys.argv[2]

    if op == '+':
        result = a + b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        result = a/b
    else:
        print("Invalid operator: '{}'".format(op))
        exit()
    print(result)

if __name__ == '__main__':
    main()

