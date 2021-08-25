"""
Use list as queue
"""


def main():
    a_queue = []
    print(a_queue)                     # []

    a_queue.append('Moo')
    print(a_queue)                    # ['Moo']

    a_queue.append('Bar')
    print(a_queue)                    # ['Moo', 'Bar']

    first = a_queue.pop(0)
    print(first)                      # Moo
    print(a_queue)                    # ['Bar']


if __name__ == '__main__':
    main()