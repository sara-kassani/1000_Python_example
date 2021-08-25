"""
stack with deque
"""


def main():
    from collections import deque
    stack = deque()

    stack.append('Joe')
    stack.append('Jane')
    stack.append('Bob')


    while stack:
        name = stack.pop()
        print(name)


                                                    # Bob
                                                    # Jane
                                                    # Joe


if __name__ == '__main__':
    main()


