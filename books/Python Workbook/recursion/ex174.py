# exercise 174: Greatest Common Divisor

def find_gcd(a, b):
    # BASE CASE
    if b == 0:
        return a
    # RECURSIVE CASE
    else:
        c = a % b
        return find_gcd(b, c)


if __name__ == '__main__':
    print(find_gcd(0, 10))
