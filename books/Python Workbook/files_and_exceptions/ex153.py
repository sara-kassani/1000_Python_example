# exercise 153: Find the Longest Word in a File

import os.path


input_file = input('please enter file name: ')
file_to_open = os.path.join("..", "files", input_file)
fin = open(file_to_open, 'r')

last_length = 0

words = []

# the first loop is on each line
for line in fin:
    # gradually searching longest words dividing each line in a list of words and looping on the list
    for el in line.split():
        if len(el) > last_length:
            words = [el]
            last_length = len(el)
        elif len(el) == last_length:
            if el not in words:
                words.append(el)


print('length of longest word(s): %d' % last_length)
print('words: %s' % words)
