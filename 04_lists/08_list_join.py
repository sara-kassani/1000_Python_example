"""
Join
"""
def main():
    fields = ['one', 'two and three', 'four', 'five']
    together = ':'.join(fields)
    print(together)                     # one:two and three:four:five

    together = ' '.join(fields)
    print(together)                     # one two and three four five

    mixed = ' -=<> '.join(fields)
    print(mixed)                        # one -=<> two and three -=<> four -=<> five

    another = ''.join(fields)
    print(another)                      # onetwo and threefourfive

    # join list of numbers
    a = ['x', '2', 'y']
    b = ['x', 2, 'y']
    print(':'.join(a))                  # x:2:y
    print(':'.join(b))                  # TypeError:

    # Converts elements to string using map
    print(":".join(map(str, b)))


if __name__ == '__main__':
    main()