# exercise 180: String Edit Distance

"""
the edit distance is a measure of similarity
the smaller is the edit distance between two strings, the more similar they are
edit distance = minimum number of insert/delete/substitute operations needed to transform one word into the other
"""


def editDistance(s, t):
    if len(s) == 0:
        return len(t)

    elif len(t) == 0:
        return len(s)

    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1
        d1 = editDistance(s[:-1], t) + 1
        d2 = editDistance(s, t[:-1]) + 1
        d3 = editDistance(s[:-1], t[:-1]) + cost

        return min(d1, d2, d3)


def main():
    word1 = input('enter the first string: ')
    word2 = input('enter the second string: ')
    print('the edit distance between the two words is:')
    print(editDistance(word1, word2))


if __name__ == '__main__':
    main()
