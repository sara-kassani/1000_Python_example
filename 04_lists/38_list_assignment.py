"""
list assignemt
- list assignment works in "parallel" in Python
"""


def main():
    x, y = 1, 2
    print(x)
    print(y)

    x, y = y, x

    print(x)
    print(y)

    # x, y = f()      # works if f returns a list of 2 elements
    #  It   will throw a run-time ValueError exception if the number
    # of values in the returned list is not 2. (Both for fewer and for more return values).

if __name__ == '__main__':
    main()
