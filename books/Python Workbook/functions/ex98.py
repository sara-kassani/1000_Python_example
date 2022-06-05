# exercise 98: Is a Number Prime?

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_n_primes(n):
    for i in range(1, n+1):
        if isPrime(i):
            print(i)


def main():
    value = int(input('enter a number: '))
    if isPrime(value):
        print(value, 'is a prime number')
    else:
        print(value, 'is not a prime number')


if __name__ == '__main__':
    #first_n_primes(100)
    main()
