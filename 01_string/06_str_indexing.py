"""
string indexing
"""
def main():
    txt = "The black cat climbed the green tree."
    print(txt.index('bl'))
    print(txt.index('The'))
    print(txt.index('the'))
    # print(txt.index('dog'))

    # index in a string with range
    print(txt.index('c'))
    print(txt.index('c', 8))

    print(txt.index('gr', 8))

    # rindex in string with range
    print(txt.rindex('c'))
    print(txt.rindex('c', 8))
    print(txt.rindex('c', 8, 13))


if __name__ == '__main__':
    main()

