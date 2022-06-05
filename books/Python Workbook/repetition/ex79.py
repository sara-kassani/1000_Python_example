# exercise 79: Greatest Common Divisor

n = int(input('enter a positive integer n: '))
m = int(input('enter a positive integer m: '))

if n >= m:
    d = m
else:
    d = n
# shorter below
# d = min(n,m)

while n % d != 0 or m % d != 0:
    d -= 1

print('GCD:', d)
