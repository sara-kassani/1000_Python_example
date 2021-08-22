"""
Queue using deque from collections
- append
- popleft
-len() number of elements
- if q: to see if it has elements or if it is empty
"""

def main():
    from collections import deque
    items = deque(['foo', 'bar'])

    print(type(items))                                  # <class 'collections.deque'>
    print(items)                                        # deque(['foo', 'bar'])

    items.append('zorg')
    print(items)                                        # deque(['foo', 'bar', 'zorg'])
    print(len(items))                                   # 3

    items.append('zorg')
    print(items)                                        # deque(['foo', 'bar', 'zorg', 'zorg'])

    nxt = items.popleft()
    print(nxt)                                          # foo
    print(items)                                        # deque(['bar', 'zorg', 'zorg'])
    print(len(items))                                   # 3

    if items:
        print('The queue has items')                    # The queue has items
    else:
        print('The queue is empty')


if __name__ == '__main__':
    main()