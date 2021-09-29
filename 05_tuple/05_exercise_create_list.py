"""
Exercise: Create list
- Given a list of strings with words separated by spaces,
- create a single list of all the words
- then create a list of unique values sorted in alphabetical order.
"""

def main():
    lines = [
        'grape banana mango',
        'nut orange peach '
        'apple nut banana apple mango '
    ]

    one_line = ' '.join(lines)
    print(one_line)
    fruits = one_line.split()
    print(fruits)

    unique_fruits = []
    for word in fruits:
        if word not in unique_fruits:
            unique_fruits.append(word)
    print(sorted(unique_fruits))


if __name__ == '__main__':
    main()


# grape banana mango nut orange peach apple nut banana apple mango
# ['grape', 'banana', 'mango', 'nut', 'orange', 'peach', 'apple', 'nut', 'banana', 'apple', 'mango']
# ['apple', 'banana', 'grape', 'mango', 'nut', 'orange', 'peach']
