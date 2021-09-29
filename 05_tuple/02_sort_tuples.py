"""
Sort tuples
- Sorting tuples or kist, or other complex structures
"""

def main():
    students = [
        ('John', 'A', 2),
        ('Zoro', 'C', 1),
        ('Dave', 'B', 3),
    ]

    print(students)
    print(type(students))

    print(sorted(students))  # sorted by the first key (name)
    print(sorted(students, key = lambda s : s[1]))
    print(sorted(students, key = lambda s : s[2]))

    from operator import itemgetter
    # operator.itemgetter(n) constructs a callable that assumes an iterable object (e.g. list, tuple, set) as input, and fetches the n-th element out of it
    print(sorted(students, key = itemgetter(2)))
s

if __name__ == '__main__':
    main()

    # [('John', 'A', 2), ('Zoro', 'C', 1), ('Dave', 'B', 3)]
    # <
    #
    # class 'list'>
    #
    #
    # [('Dave', 'B', 3), ('John', 'A', 2), ('Zoro', 'C', 1)]        # sort by the first element of each tuple
    # [('John', 'A', 2), ('Dave', 'B', 3), ('Zoro', 'C', 1)]        # sort by the 2nd element of the tuples (index 1)
    # [('Zoro', 'C', 1), ('John', 'A', 2), ('Dave', 'B', 3)]        # sort by the 3rd element of the tuples (index 2)
    # [('Zoro', 'C', 1), ('John', 'A', 2), ('Dave', 'B', 3)]        # maybe this is more simple than the lambda version and probably faster
