# exercise 80: Prime Factors

n = int(input('enter integer: '))

factor = 2

if n < factor:
    print('error: n must be greater than 2')

while factor <= n:
    if n % factor == 0:
        print(factor)
        n = n//factor
    else:
        factor += 1