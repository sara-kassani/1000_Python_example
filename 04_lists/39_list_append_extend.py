"""
append vs. extend
- What is the difference between [].append and [].extend?
- The method append adds its parameter as a single element to the list while extend gets a list and adds its content.
"""

def main():
    names = ['Foo Bar', 'Orgo Morgo']
    more = ['Joe Doe', 'Jane Doe']

    names.extend(more)
    print(names)                            # ['Foo Bar', 'Orgo Morgo', 'Joe Doe', 'Jane Doe']

    names.append(more)
    print(names)                            # ['Foo Bar', 'Orgo Morgo', 'Joe Doe', 'Jane Doe', ['Joe Doe', 'Jane Doe']]

    names = ['Foo', 'Bar']
    names.append('Qux')
    print(names)                            # ['Foo', 'Bar', 'Qux']


    names = ['Foo', 'Bar']
    names.extend('Qux')
    print(names)                            # ['Foo', 'Bar', 'Q', 'u', 'x']


if __name__ == '__main__':
    main()