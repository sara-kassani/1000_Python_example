"""
remove items from list
- remove first element from a list given by its value
- Throw an exception if there is no such element in the list
- Use del to remove an element by index, 
- Use pop() to remove it by index if you need the returned value, 
- Use remove() to delete an element by value. The last requires searching the list, and raises ValueError if no such value occurs in the list.
"""

def main():
    names = ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']
    print(names)

    print(names.remove('Kim'))             # None
    print(names)                           # ['Joe', 'Jane', 'Bob', 'Kim'] --> first kim is removed

    # print(names.remove('George'))        # Error: Traceback ...

    # remove element by pop
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
    print(planets)

    third = planets.pop(2)
    print (third)                           # Earth
    print(planets)                          # ['Mercury', 'Venus', 'Mars', 'Jupiter']

    last = planets.pop()
    print(last)                             # Jupiter
    print(planets)                          # ['Mercury', 'Venus', 'Mars']

    # planets.pop(4)                        # IndexError: pop index out of range

    jupyter_landers = []
    jupyter_landers.pop()                   # IndexError: pop from empty list

    # remove first elements of list
    names = ['foo', 'bar', 'baz', 'moo']

    first = names.pop(0)
    print(first)
    print(names)

    # Remove several elements of list by index (use the slice syntax)
    names = ['foo', 'bar', 'baz', 'moo', 'qux']

    names[2:4] = []
    print(names)                            # ['foo', 'bar', 'qux']


if __name__ == '__main__':
    main()
