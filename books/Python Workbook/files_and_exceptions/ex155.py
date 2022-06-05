# exercise 155: Words that Occur Most

from lists.ex117 import words_in_string

from pathlib import Path


# the path to the folder with all files inside it, it will be used as base where to add the file name
data_folder = Path("../files/")

text = input('enter text or book: ')
# the file to read will be given by the file path to the folder of files plus the file name
fin = open(data_folder / text, 'r')
d = dict()

for line in fin:
    for word in words_in_string(line):
        word = word.lower()
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
# inverting keys and values to have frequencies as keys and list of words as values
inverse = dict()
for key in d:
    if d[key] not in inverse:
        inverse[d[key]] = [key]
    else:
        inverse[d[key]].append(key)

#print(inverse)

# sorting the reversed dictionary, which was in its turn reversed based on higher frequencies
# in this way I will have the most frequent words above
for key in reversed(sorted(inverse)):
    # if one word only is associated to highest frequency, there will be no parentheses
    if len(inverse[key]) == 1:
        print(inverse[key][0], '>>>', key)
        break
    else:
        print(inverse[key], '>>>', key)
        break
    # the break in both cases allow to print only the first highest frequency and then exit from the loop
