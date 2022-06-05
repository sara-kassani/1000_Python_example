# exercise 143: Anagrams

# solution through function which has one parameter and is invoked on two strings (logic in main function)
def histogram(s):
    s = s.upper()
    h = {}

    for c in s:
        if c not in h:
            h[c] = 1
        else:
            h[c] += 1

    return h


def main():
    word1 = input('enter the first word: ')
    word2 = input('enter the second word: ')

    if histogram(word1) == histogram(word2):
        print('those words are anagrams')
    else:
        print('those words are NOT anagrams')


if __name__ == '__main__':
    main()

"""
the words are anagrams if their histograms letters-frequences are equal
dictionaries are equal if they have the same keys and values independently from the order
"""
