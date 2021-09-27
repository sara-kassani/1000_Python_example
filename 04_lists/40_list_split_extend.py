"""
split and extend
- when collecting data which is received from a string via splitting, we would like to add the new elements to the existing list
"""


def main():
    lines = [
        'abc def ghi',
        'hello world',
    ]

    collector = []

    for l in lines:
        collector.extend(l.split())
        print(collector)


if __name__ == '__main__':
    main()


# ['abc', 'def', 'ghi']
# ['abc', 'def', 'ghi', 'hello', 'world']
