"""
printf using old %-syntax
"""


def main():
    v = 65
    print('<%s>' % v)           # <65>
    print('<%10s>' % v)         # <        65>
    print('<%-10s>' % v)        # <65        >
    print('<%c>' % v)           # <A>
    print('<%d>' % v)           # <65>
    print('<%0.5d>' % v)        # <00065>


if __name__ == '__main__':
    main()