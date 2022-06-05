# exercise 167: Spell Checker

"""
due to the structure of the project (root directory python_worbook),
the script has to be launched from CLI from the root directory
and the command will be:
python -m files_and_exceptions.ex167 file1.txt file2.txt
"""

from lists.ex117 import words_in_string

import sys
from pathlib import Path


def check_misspelled(myfile, base_file):
    misspelled = []
    # reading a base file containing all possible words
    # from that file I create a dictionary where each key is a word
    all_words_file = open(base_file, 'r')
    all_words_d = dict()
    for line in all_words_file:
        line = line.strip()
        all_words_d[line] = 0

    all_words_file.close()

    # reading the file upon which I have to make the check
    # looping each word of the file ignoring punctuation and case
    # if the single looped word is not present in the base dictionary, then is a misspelled
    # pushing the misspelled in the output list, only if not already present
    myf = open(myfile, 'r')
    for line in myf:
        for word in words_in_string(line):
            if word.lower() not in all_words_d and not word.isdigit():
                if word.lower() not in misspelled:
                    misspelled.append(word)
    myf.close()

    return misspelled


def main():
    data_folder = Path('files')
    if len(sys.argv) != 3:
        print('please insert three parameters in command line')
        quit()

    # passing through CLI the files upon which to make the comparison
    # after the script, the first passed file will be the one to check, while the latter contains all words
    try:
        for word in check_misspelled(data_folder / sys.argv[1], data_folder / sys.argv[2]):
            print(word, end='  ')

    except:
        print('something went wrong: try checking the name of the files')


if __name__ == '__main__':
    main()