"""
for-in loop
"""
def main():
    # for-in loop on strings
    txt = 'hello world'
    for ch in txt:
        print(ch)

    # for-in loop on list
    for fruit in ['Apple', 'Banana', 'Peach', 'Orange', 'Durian', 'Papaya']:
        print(fruit)

    # for-in loop on range
    for ix in range(3, 7):
        print(ix)


if __name__ == '__main__':
    main()