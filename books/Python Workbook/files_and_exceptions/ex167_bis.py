# exercise 167: Spell Checker

from lists.ex117 import words_in_string
import sys
from pathlib import Path

"""
due to the structure of the project, the script has to be launched from CLI
starting from the root directory python_workbook and typing the following command:
python -m files_and_exceptions.ex167_bis emma.txt words.txt
Since the script is launched from CLI, in the main() program, and after the try statement,
I will use as starting data folder the file path "files" because that is a direct subdirectory
of root directory. Then to that data folder each of the two CLI arguments will be added 
(e.g. files/emma.txt files/words.txt).
"""


# in this version I use a set (in the place of a dictionary) where I store all possible words
# I also replace all the '--' in the text with a space, since many words between '--' are existing words
# note: using words_a_i.txt instead of words.txt as base_file will count 'a' and 'I' as existing words

def check_misspelled(myfile, base_file):
    misspelled = []

    all_words_file = open(base_file, 'r')
    # I create a set of all words
    all_words_d = set()
    for line in all_words_file:
        line = line.strip()
        all_words_d.add(line)

    all_words_file.close()

    myf = open(myfile, 'r')
    for line in myf:
        for word in words_in_string(line):
            if word.lower() not in all_words_d and not word.isdigit():
                if word.lower() not in misspelled:
                    misspelled.append(word)
    myf.close()

    return misspelled


def main():
    if len(sys.argv) != 3:
        print('please insert three parameters in command line')
        quit()

    try:
        data_folder = Path("files")
        for word in check_misspelled(data_folder / sys.argv[1], data_folder / sys.argv[2]):
            print(word)

    except:
        print('something went wrong: try checking the name of the files')


if __name__ == '__main__':
    main()