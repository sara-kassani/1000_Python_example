# exercise 162: A Book With No E...

from lists.ex117 import words_in_string

from pathlib import Path


data_folder = Path("../files/")
filename = input('enter a file to open: ')
inf = open(data_folder / filename, 'r')
words = []

for line in inf:
    line = line.strip()
    words += words_in_string(line)

# until here I have a list of all the words from the file.txt

words_tot_num = len(words)

# pushing in a list all letters from a to z
letters = []
for i in range(97, 123):
    letters.append(chr(i))

proportions = []
counters = []

for letter in letters:
    counter = 0
    for word in words:
        if letter in word.lower():
            counter += 1
    proportion = (counter / words_tot_num) * 100
    proportions.append('%.1f %%' % proportion)

# until here I will have two lists: a list of letters and a list of proportions
# what I can do is creating a dictionary key-value where I map letters to proportions
# to do it I use zip()

d = dict(zip(letters, proportions))
# printing letters and proportions
# note: the proportions give info about the percentage of words that contain a given letter
for k in d:
    print(k, '>>>', d[k])

# finding the letter with the lowest proportion
min_prop = min(proportions)
smallest_prop_letter = letters[proportions.index(min_prop)]
print('the letter with the smallest proportion is:\n%s >>> %s' % (smallest_prop_letter, min_prop))

"""tip:
if I do not ignore the case, I see that proportion of letter 'i' falls down a lot
this is because very often letter i appears in uppercase when used as a word 'I'
"""
