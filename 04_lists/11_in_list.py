"""
in list
check if the value is in the list
"""
def main():
    words = ['apple', 'banana', 'peach', '42']
    if 'apple' in words:
        print('found!')

    if 'a' in words:
        print('found')
    else:
        print('NOT found!')

    if 42 in words:
        print('found 42')
    else:
        print('NOT found!')


if __name__ == '__main__':
    main()