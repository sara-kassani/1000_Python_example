# exercise 162: A Book With No E...

"""
this solution is applicable only to the words.txt file or any other file which includes a word per-line
"""

from pathlib import Path


file_to_open = Path("../files/words.txt")
words_count = 0

# creating a dictionary with each letter as a key and its frequency (starting from zero) as a value
contains = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in letters:
    contains[letter] = 0

# opening file and processing each word (in the file words.txt each line only has one word)
inf = open(file_to_open, 'r')
for word in inf:
    # the right strip removes the newline character
    word = word.upper().rstrip()

    # before counting the frequency of each word's letter, we have to consider the "unique" letters in that word
    unique = []
    for ch in word:
        if ch not in unique and ch != '-':
            unique.append(ch)

    for ch in unique:
        contains[ch] += 1

    words_count += 1

inf.close()

# finding smallest and highest frequency
smallest_count = min(contains.values())
highest_count = max(contains.values())

if __name__ == '__main__':
    print('words count: {}'.format(words_count))
    print('here is each letter with the number of words containing it:')
    print(contains)
    print()
    for letter in sorted(contains):
        percent = contains[letter] / words_count * 100
        percent = '%.2f' % percent
        if contains[letter] == smallest_count:
            print('{} is in {} % of words --> least words include this character'.format(letter, percent))
        elif contains[letter] == highest_count:
            print('{} is in {} % of words --> most words include this character'.format(letter, percent))
        else:
            print('{} is in {} % of words'.format(letter, percent))
