"""
List operators
"""


def main():
    a = ['one', 'two']
    b = ['three']

    print( a * 2)
    print(2 * a)

    print(a + b)
    print(b + a)


if __name__ == '__main__':
    main()

# ['one', 'two', 'one', 'two']
# ['one', 'two', 'one', 'two']
# ['one', 'two', 'three']
# ['three', 'one', 'two']
