"""
while loop
"""
def main():
    import random

    total = 0
    while total <= 100:
        print(total)
        total += random.randrange(20)
    print("Done")

    # infinite while loop
    total = 0
    while total >= 0:
        print(total)
        total += random.randrange(20)
    print("Done")

    # while with complex expressiin
    total = 0
    while (total < 10000000) and (total % 17 !=1) and (total ** 2 % 23 !=7):
        print(total)
        total += random.randrange(20)

        print('done')

    # while with break with break
    random.seed(0)

    total = 0
    while total < 10000000:
        print(total)
        total += random.randrange(20)

        if total % 17 == 1:
            break

        if total ** 2 % 23 == 7:
            break
    print('done')

    # while true
    random.seed(0)

    total = 0
    while True:
        print(total)
        total += random.randrange(20)

        if total >= 10000000:
            break

        if total % 17 == 1:
            break

        if total ** 2 % 23 == 7:
            break

    print('done')

if __name__ == '__main__':
    main()