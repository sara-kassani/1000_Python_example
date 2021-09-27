"""
List of lists
"""


def main():
    x = ['abc', 'def']
    print(x)

    y = [x, 'xyz']
    print(y)
    print(y[0])

    print(x[0])
    print(y[0][0])


if __name__ == '__main__':
    main()

    # ['abc', 'def']
    # [['abc', 'def'], 'xyz']
    # ['abc', 'def']
    # abc
    # abc
