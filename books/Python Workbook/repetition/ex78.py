# exercise 78: The Collatz Conjecture

n = int(input('enter a positive integer: '))

while n > 0:
    sequence = str(n)
    current = n
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = (current * 3) + 1
        sequence += ' %s' % current

    print(sequence)

    n = int(input('enter a positive integer: '))

