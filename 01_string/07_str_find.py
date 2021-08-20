"""
find in string
"""
def main():
    txt = 'The black cat climbed the green tree'
    print(txt.find('bl'))
    print(txt.find('The'))
    print(txt.find('dog'))

    print(txt.find('c'))
    print(txt.find('c', 8))

    print(txt.find('gr', 8))
    print(txt.find('gr', 8, 16))

    print(txt.rfind('c', 8))

    # find all in the string
    txt = 'hello world'
    if 'wo' in txt:
        print('found wo')

    if 'x' in txt:
        print('found x')
    else:
        print('NOT found x')

    # index if in string
    sub = 'dog'
    txt = 'The black cat climbed the green tree'

    if sub in txt:
        loc = txt.index(sub)
        print(sub + 'is at' + str(loc))

    sub = 'dog'
    if sub in txt:
        loc = txt.find(sub)
        print(sub + 'is at ' + str(sub))


if __name__ == '__main__':
    main()