# exercise 133: Does a List Contain a Sublist?

def isSublist(larger, smaller):
    if smaller == [] or smaller == larger:
        return True
    """
    if smaller[0] in larger and len(smaller) == 1:
        return True
    """
    if smaller[0] not in larger or len(smaller) > len(larger):
        return False

    else:

        check = True
        # looping each element to find the elements that are equal to the first of smaller inside the larger list
        for i in range(len(larger)):
            if larger[i] == smaller[0]:
                sub_i = i + 1
                for j in range(1, len(smaller)):
                    if smaller[j] != larger[sub_i]:
                        check = False
                        break
                    else:
                        check = True
                    sub_i += 1
                # at the end of the loop I check if the value of check is still True
                if check:
                    return True
        return False


def main():
    print(isSublist([1, 2, 3, 4], []))
    print(isSublist([1, 2, 3, 4], [1]))
    print(isSublist([1, 2, 3, 4], [1, 2]))
    print(isSublist([1, 2, 3, 4], [2, 4]))
    print(isSublist([1, 2, 3, 4], [3, 4]))
    print(isSublist([10, 2, 35, 47, 10, 2, 36, 46, 10, 2, 35, 45, 46], [10, 2, 35, 46]))
    print(isSublist([10, 2, 35, 47, 10, 2, 36, 46, 10, 2, 35, 45, 46], [10, 2, 35, 45, 46]))
    print(isSublist([10, 2, 35, 47, 10, 2, 36, 46, 10, 2, 35, 45, 46], [10, 2, 35, 45, 45, 46]))


if __name__ == '__main__':
    main()
