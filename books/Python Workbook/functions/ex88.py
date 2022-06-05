# exercise 88: Median of Three Values

def find_median(a, b, c):
    low = min(a, b, c)
    high = max(a, b, c)
    if a != low and a != high:
        return a
    if b != low and b != high:
        return b
    if c != low and c != high:
        return c

    if a == b and a == c:
        return a  # or return b or return c

    if a != b and a != c:
        return b  # or return c

    if b != a and b != c:
        return a  # or return c

    if c != a and c != b:
        return a  # or return b


# alternative optimised version
def alternate_median(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


def main():
    a = float(input('enter a value: '))
    b = float(input('enter b value: '))
    c = float(input('enter c value: '))
    print('median is %d' % find_median(a, b, c))
    print('median is %d' % alternate_median(a, b, c))


if __name__ == '__main__':
    main()



