"""
Exercise: count digits
- Given a list of numbers numbers = [1203, 1256, 312456, 98 ,
- count how many times each digit appears? The output will look like this:
1 0 1
2 1 3
3 2 3
4 3 2
5 4 1
6 5 2
7 6 2
8 7 0
9 8 1
10 9 1
"""

def main():
    numbers = [1203, 1256, 312456, 98]

    count = [0] * 10        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in numbers:
        for char in str(num):
            count[int(chr)] += 1

    for d in range(0, 10):
        print('{]   {}'.format(d, count[d]))


if __name__ == '__main__':
    main()
