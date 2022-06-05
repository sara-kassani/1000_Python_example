# exercise 111: Reverse Order

t = []

n = int(input('enter integer (0 to quit): '))

while n != 0:
    t.append(n)
    n = int(input('enter integer (0 to quit): '))

t.sort()
i = len(t)-1
while i >= 0:
    print(t[i])
    i -= 1
