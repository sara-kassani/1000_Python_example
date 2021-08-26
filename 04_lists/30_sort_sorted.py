"""
sort with sorted
- sort: The sort() method will sort a list in-place and return None
- sorted: The built-in sorted() function will return the sorted list and leave the original list intact.
"""

def main():
    animals = ['chicken', 'cow', 'snail', 'elephant']
    print(animals)              # ['chicken', 'cow', 'snail', 'elephant']
    s = sorted(animals)
    print(s)                    # ['chicken', 'cow', 'elephant', 'snail']
    print(sorted)               # <built-in function sorted>

    r = sorted(animals, reverse = True, key = len)
    print(r)                    # ['elephant', 'chicken', 'snail', 'cow']
    print(animals)              # ['chicken', 'cow', 'snail', 'elephant']


if __name__ == '__main__':
    main()