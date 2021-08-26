"""
key sort
- another example for using a key
- to sort the list according to length
"""

def main():
    animals = ['chicken', 'cow', 'snail', 'elephant']
    print(animals)                  # ['chicken', 'cow', 'snail', 'elephant']

    animals.sort()
    print(animals)                  # ['chicken', 'cow', 'elephant', 'snail']

    animals.sort(key = len)
    print(animals)                  # ['cow', 'snail', 'chicken', 'elephant']

    animals.sort(key = len, reverse = True)     # ['elephant', 'chicken', 'snail', 'cow']
    print(animals)


if __name__ == '__main__':
    main()