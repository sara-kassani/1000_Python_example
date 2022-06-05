# exercise 95: Capitalize It

def capitalize(s):
    li = list(s)
    li[0] = li[0].upper()
    c = 1
    for c in range(1, len(li)):
        if li[c] == 'i' and li[c - 1] == ' ' and li[c + 1] == ' ':
            li[c] = li[c].upper()
        if li[c] == '.' or li[c] == '!' or li[c] == '?':
            if c + 2 < len(li):
                li[c + 2] = li[c + 2].upper()
    res = ''
    for el in li:
        res += el
    return res


def main():
    string = input('please enter: ')
    print(capitalize(string))


if __name__ == '__main__':
    main()
