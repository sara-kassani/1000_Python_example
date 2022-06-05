# exercise 144: Anagrams Again

def histogram(s):
    ignore_list = ['.', ',', ':', ';', '"', '?', '!', ' ', '<<', '>>']
    s = s.upper()
    h = {}

    for c in s:
        # adding to the histograms only characters which are not in ignore list
        if c not in ignore_list:
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
