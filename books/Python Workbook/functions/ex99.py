# exercise 99: Next Prime

from functions.ex98 import isPrime


def nextPrime(n):
    i = n+1
    while True:
        if isPrime(i):
            return i
        i += 1


def main():
    value = int(input('enter a number: '))
    print('the first prime after {} is {}'.format(value, nextPrime(value)))


if __name__ == '__main__':
    main()
