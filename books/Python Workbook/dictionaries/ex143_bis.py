# exercise 143: Anagrams

# solution through function which takes the two words as parameters
def isAnagram(word1, word2):
    d1 = {}
    d2 = {}

    for c in word1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c] += 1

    for c in word2:
        if c not in d2:
            d2[c] = 1
        else:
            d2[c] += 1
    #print(d1)
    #print(d2)

    if d1 == d2:
        return True

    return False


def is_anagram_shorter(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))


def main():
    print(isAnagram('skate', 'takes'))
    print(is_anagram_shorter('takes', 'skate'))


if __name__ == '__main__':
    main()





