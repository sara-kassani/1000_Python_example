"""
Fixed size queue
"""

def main():
    from collections import deque
    queue = deque([], maxlen= 3)
    print(queue.maxlen)             # 3

    queue.append('Foo')
    queue.append('Bar')
    queue.append('Baz')
    print(queue)                    # deque(['Bar', 'Baz', 'Zorg'], maxlen=3)

    queue.append('Zorg')
    print(queue)                    # deque(['Foo', 'Bar', 'Baz'], maxlen=3)


if __name__ == '__main__':
    main()