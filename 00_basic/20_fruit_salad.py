"""
Exercise: Fruit salad
- write a script that will pick 3 fruits from a list of fruits and print them.
- these fruits should be different.
"""

import random
def main():
    fruits = ['Apple', 'Banana', 'Peach', 'Orange', 'Durian', 'Papaya']
    salad = random.sample(fruits, 3)
    print(salad)      # ['Papaya', 'Banana', 'Peach']

if __name__ == '__main__':
    main()
