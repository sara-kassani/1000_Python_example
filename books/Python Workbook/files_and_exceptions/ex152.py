# exercise 152: Number the Lines in a File

from pathlib import Path


data_folder = Path("../files")
file_to_read = data_folder / 'words.txt'
file_to_create = data_folder / 'words_numbered.txt'

fin1 = open(file_to_read, 'r')
fin2 = open(file_to_create, 'w')
# mode 'w' overwrites the content, if the file exists, otherwise it creates a new file with that content
# instead, if I used mode 'a', the content would be added to the end of the file
# if the file that I want to edit is empty, it does not change anything between 'w' and 'a'

i = 1

for x in fin1:
    fin2.write("%d: %s" % (i, x))
    i += 1

fin1.close()
fin2.close()

display = open('words_test_numbered.txt', 'r')

for num_line in display:
    num_line = num_line.rstrip()
    print(num_line)

""" or
for el in display.readlines():
    print(el.rstrip())
"""

display.close()
