"""
Debugging Queue
"""

q = []
while True:
    name = input('Your name: ')

    if name == 'n':
        print(q.pop(0))

    if name == 'x':
        print(q)
        exit()

    if name == 's':
        print(len(q))
        exit()

    else:
        q.append(name)
        continue