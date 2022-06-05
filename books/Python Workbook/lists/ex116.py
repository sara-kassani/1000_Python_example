# exercise 116: Perfect Numbers

from lists.ex115 import proper_divisors


def isPerfect(n):
    return n == sum(proper_divisors(n))


# the program looks for all perfect numbers between 1 and 10000 (4 in total)
def main():
    print(isPerfect(28))
    for i in range(1, 10000):
        if isPerfect(i):
            print(i)


if __name__ == '__main__':
    main()
