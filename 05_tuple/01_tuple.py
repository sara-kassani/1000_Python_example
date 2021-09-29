"""
tuple
- a tuple is a fixed-length immutable list. It cannot change its size or content.
- a tuple is denoted with parentheses

- elements of a list can be changed via their index or via the list slice notation
- a list can grow and shrink using append and pop methods or using a slice notation
- A list is denoted with square brackets: [1, 2, 3]

Notes:
    - Tuples are rarely used (You don't need to use them). There are certain places wher Python or some module require tuple (instead of lists) or return a tuple (instead of list)
    - key dictioneries can be tuple (but not lists)
"""


def main():
    t = ('a', 'b', 'c')
    print(t)                            # ('a', 'b', 'c')

    l = ['abc', 'def', 'ghi']

    t = tuple(l)
    print(l)                            # ['abc', 'def', 'ghi']
    print(t)                            # ('abc', 'def', 'ghi')


if __name__ == '__main__':
    main()
