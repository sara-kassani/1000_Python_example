"""
Exercise: Check if number is prime
- write a progran that gets a number on the command ine, prints 'True' if the number is a prime number or 'False' if it isn't
"""


def main():
    import math
    # import sys
    # n = int(sys.argv[1])

    n = int(input('Enter a number: '))
    print(n)

    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        # for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)


if __name__ == '__main__':
    main()
