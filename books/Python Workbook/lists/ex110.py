# exercise 110: Sorted Order

t = []
while True:
    value = int(input('enter value: '))
    if value == 0:
        break
    t.append(value)

for el in sorted(t):
    print(el)
