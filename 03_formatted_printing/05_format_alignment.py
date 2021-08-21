"""
Examples using format - alignment
"""


def main():
    txt = 'Some text'

    print("'{}'".format(txt))        # as default
    print("'{:12}'".format(txt))     # left
    print("'{:<12}'".format(txt))    # left
    print("'{:>12}'".format(txt))    # right
    print("'{:^12}'".format(txt))    # center


if __name__ == '__main__':
    main()