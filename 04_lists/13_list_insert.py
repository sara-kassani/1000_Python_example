"""
insert into list
"""


def main():
    lst = ['apple', 'banana', 'cat']
    print(lst)

    lst.insert(2, 'zebra')
    print(lst)

    lst.insert(0, 'dog')
    print(lst)

    # instead of insert, use  append
    lst.insert(len(lst), 'olifant')
    print(lst)


if __name__ == '__main__':
    main()


