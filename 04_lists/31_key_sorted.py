"""
key sort with sorted
- To sort the list according to length using sorted
"""

def main():
    animals = ['snail', 'cow', 'elephant', 'chicken']
    animals_in_abc = sorted(animals)                        # ['snail', 'cow', 'elephant', 'chicken']

    print(animals)
    print(animals_in_abc)                                  # ['chicken', 'cow', 'elephant', 'snail']

    animals_by_length = sorted(animals, key = len)
    print(animals_by_length)                               # ['cow', 'snail', 'chicken', 'elephant']


if __name__ == '__main__':
    main()
