"""
Exercise: Queue
The application should manage a queue of people.
        - it will prompt the user for a new name by printing:, the user can type in name and press ENTER. The app will add the name to the queue.
        - if the user type in "n", then the application will remove the first name from queue and print it.
        - if the user type in "x" then the application will print the list of users who were left in the queue anf it will exit.
        - if the users types in "s" then the application will show the current number of elements in the queue.
"""

def main():
    # Solution: Queue with list

    queue = []
    while True:
        inp = input(':')
        inp = inp.rstrip('\n')

        if inp == 'x':
            for name in queue:
                print(name)
            exit()

        if inp == 's':
            print(len(queue))
            continue

        if inp == 'n':
            if len(queue) > 0:
                print('next is {}'. format(queue.pop(0)))
            else:
                print('The queue is empty')
                continue
        queue.append(inp)


    # Solution: Queue with deque
    from collections import deque

    queue = deque()
    while True:
        inp = input(':')
        inp = inp.rstrip('\n')

        if inp == 'x':
            for name in queue:
                print(name)
            exit()

        if inp == 's':
            print(len(queue))
            continue

        if inp == 'n':
            if len(queue) > 0:
                print('next is {}'.format(queue.popleft()))
            else:
                print('The queue is empty')
            continue


if __name__ == '__main__':
    main()
