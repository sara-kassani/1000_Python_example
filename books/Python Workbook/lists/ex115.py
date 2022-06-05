# exercise 115: List of Proper Divisors

def proper_divisors(n):
    list_of_divisors = []
    for i in range(1, n):
        if n % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors


def main():
    number = int(input('enter integer: '))
    print(proper_divisors(number))


if __name__ == '__main__':
    main()
