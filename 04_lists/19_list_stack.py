"""
List as a stack
"""


def main():
    stack = []

    stack.append('Joe')
    print(stack)                        # ['Joe']

    stack.append('Jane')
    print(stack)                        # ['Joe', 'Jane']

    stack.append('Bob')
    print(stack)                        # ['Joe', 'Jane', 'Bob']

    while stack:
        name = stack.pop()
        print(name)
        print(stack)

        # Bob
        # ['Joe', 'Jane']
        # Jane
        # ['Joe']
        # Joe
        # []

if __name__ == '__main__':
    main()


