"""
Change a list
- Unlike strings, lists are mutable.
- Use the slice notation to change several elements at once
- you can even have different number of elements in the slice and in the replacement. This will change the length of the array.
"""


def main():
    fruits = ['apple', 'banana', 'peach', 'strawberry']
    print(fruits)                                   # ple', 'banana', 'peach', 'strawberry']

    fruits[0] = 'orange'
    print(fruits)                                   # ['orange', 'banana', 'peach', 'strawberry']

    fruits[1:3] = ['grape', 'kiwi']
    print(fruits)                                   # ['orange', 'grape', 'kiwi', 'strawberry']

    fruits[1:3] = ['mango']
    print(fruits)                                   # ['orange', 'mango', 'strawberry']

    fruits[1:2] = ['banana', 'peach']
    print(fruits)                                   # ['orange', 'banana', 'peach', 'strawberry']

    fruits = ['orange', 'mango', 'strawberry']
    fruits[1:2] = ['banana', 'peach']
    print(fruits)                                   # ['orange', 'banana', 'peach', 'strawberry']

    fruits = ['orange', 'mango', 'strawberry']
    fruits[1] = ['banana', 'peach']
    print(fruits)                                   # ['orange', ['banana', 'peach'], 'strawberry']


if __name__ == '__main__':
    main()