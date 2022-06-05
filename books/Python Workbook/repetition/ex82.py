# exercise 82: Decimal to Binary

num = int(input('enter decimal number: '))
res = ''
q = num

r = q % 2
res = str(r) + res
q = q // 2

while q > 0:
    r = q % 2
    # note that writing res += str(r) would me a mistake
    res = str(r) + res
    q = q // 2

print(res)
