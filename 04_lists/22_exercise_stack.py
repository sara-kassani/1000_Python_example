"""
Exercise: Stack
Implement a Reverse Polish Calculator
"""

def main():
    stack = []
    print('x = eXit, s = show, [+-*/]')
    while True:
        val = input(':')

        if val == 's':
            print(stack)
            continue

        if val == 'x':
            break

        if val == '+':
            a= stack.pop()
            b= stack.pop()
            stack.append(a+b)
            continue

        if val == '-':
            a= stack.pop()
            b= stack.pop()
            stack.append(a-b)
            continue

        if val == '*':
            a= stack.pop()
            b= stack.pop()
            stack.append(a*b)
            continue

        if val == '/':
            a= stack.pop()
            b= stack.pop()
            stack.append(a/b)
            continue

        if val == '=':
            print(stack.pop())
            continue

        stack.append(float(val))



    # Solution: Reverse Polish calculator (stack) with deque
    from collections import deque
    stack= deque()

    while True:
        val = input(':')
        if val == 'x':
            break

        if val == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
            continue

        if val == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a-b)
            continue

        if val == '=':
            print(stack.pop())
            continue

        stack.append(float(val))


if __name__ == '__main__':
    main()
