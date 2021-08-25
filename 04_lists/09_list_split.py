"""
Split
- Special case: To split a string to its character: Use the list() function.
- Split using more than one splitter: use re.split
"""
def main():
    words = 'ab:cd::ef'.split(':')
    print(words)                            # ['ab', 'cd', '', 'ef']

    # special case: split by spaces
    names = 'foo bar baz'.split()
    print(names)                            # ['foo', 'bar', 'baz']

    # special case: split to characters
    chars = list('ab cd')
    print(chars)                            # ['a', 'b', ' ', 'c', 'd']


if __name__ == '__main__':
    main()


