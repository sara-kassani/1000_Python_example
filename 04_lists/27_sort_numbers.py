"""
Sort numbers
"""

def main():
    numbers = [7, 2, -4, 19, 8]
    print(numbers)

    numbers.sort()
    print(numbers)

    numbers.sort(key = abs, reverse = True)
    print(numbers)


if __name__ == '__main__':
    main()