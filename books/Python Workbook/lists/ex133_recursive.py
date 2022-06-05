# exercise 133: Does a List Contain a Sublist?

def isSublist(smaller, larger):
    # BASE CASES
    if smaller == []:
        return True

    if len(larger) < len(smaller):
        return False

    index = 0
    for i in range(len(smaller)):
        if smaller[index] != larger[index]:
            break
        if index == len(smaller) - 1:
            return True
        index += 1

    # RECURSIVE CASE
    return isSublist(smaller, larger[1:])


def main():
    l1 = [1, 2, 4]
    l2 = [1, 2, 3, 4, 2, 3, 5, 1, 2, 4, 6, 2, 3, 4, 8]

    print(isSublist(l1, l2))


if __name__ == '__main__':
    main()
