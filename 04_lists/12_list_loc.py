"""
Where is the element in the list
if-in
"""


def main():
    lst = ['cat', 'dog', 'snake', 'camel']
    print(lst.index('snake'))

    print(lst.index('pyton'))

    # index improved
    name = 'snake'
    if name in lst:
        print(lst.index(name))

    name = 'python'
    if name in lst:
        print(lst.index(name))


if __name__ == '__main__':
    main()