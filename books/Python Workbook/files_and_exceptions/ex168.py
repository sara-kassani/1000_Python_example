# exercise 168: Repeated Words

from lists.ex117 import words_in_string
import sys
from pathlib import Path


"""
to launch from CLI, go to the root directory python_workbook, then use the command:
python -m files_and_exceptions.ex168 file.txt
"""

def findDuplicates(myfile):
    duplicates = []

    try:
        inf = open(myfile, 'r')

        # saving each "previous" word in a variable
        # I manage to analyse duplicates between continuous lines by using the variable outside both loops
        last_word = ''

        # looping each line of the file ignoring potential spaces to right and left
        for line in inf:
            line = line.strip()

            # looping each word inside the line/string ignoring punctuation and case through the imported function
            for word in words_in_string(line):
                # in case the current word, edited, is equal to the previous, that is a duplicate
                if word == last_word:
                    duplicates.append(word)
                # independently from condition I will always save each looped word in the variable
                last_word = word

        return duplicates

    # showing a customised error only in case the file name is wrong
    except FileNotFoundError:
        return 'error: file not found'


def main():
    # using the above function but passing the argument (file to read) from CLI
    if len(sys.argv) != 2:
        print('error: please provide two arguments')
        quit()

    data_folder = Path("files")

    print("here is the list of duplicates:")
    print(findDuplicates(data_folder / sys.argv[1]))


if __name__ == '__main__':
    main()


""" note:
initially did not manage to count duplicates between end of line and start of the next line.
The problem was adding the empty last_word variable inside the first loop. Doing so, when analysing
a new line, the variable was empty again. 
Placing the variable outside both loops, the program always manages to store the previous word
and compare it with the next encountered word.
"""