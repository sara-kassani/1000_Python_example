"""
Looping over index
"""


def main():
    things = ['abc', 'def', 'ghi', 42]

    for var in things:
        print(var)

    for i in range(len(things)):
        print(i, things[i])


if __name__ == '__main__':
    main()

# abc
# def
# ghi
# 42


# 0 abc
# 1 def
# 2 ghi
# 3 42
