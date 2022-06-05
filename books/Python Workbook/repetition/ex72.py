# exercise 72: Fizz-Buzz

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('fizz and buzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)

