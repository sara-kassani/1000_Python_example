# exercise 172: Words with Six Vowels in Order

"""before reading the file to find all words that contains all vowels appearing once and in order,
firstly I define two different functions that will be applied to each word read in the file opened.
If a word contains all vowels (first function), I use the second function to check if all that vowels appear
once and ordered inside that word. Only if both conditions are satisfied, I append that word to the output list.
Note: vowels considered are 'aeiouy'. To get rid of y, remove it from the variable vowels inside both functions.
"""

from pathlib import Path


# the function check if a string contains all vowels (a,e,i,o,u,y)
def contains_all_vowels(s):
    vowels = 'aeiouy'
    for vowel in vowels:
        if vowel not in s:
            return False
    return True


# if a string has all vowels, I use this function to check if they are present ONCE and IN ORDER
def once_and_ordered(s):
    res = ''
    vowels = 'aeiouy'
    for c in s:
        if c in vowels:
            res += c

    if res == vowels:
        return True
    else:
        return False


def main():
    data_folder = Path("../files")
    file_name = input('enter a file name: ')
    try:
        inf = open(data_folder / file_name, 'r')
    except:
        print('file not found')
        quit()

    # this is the list that will contains all the words that respect the requirement. It might also remain empty.
    words_res = []

    # looping each line of the file
    for line in inf:
        line = line.strip()
        # inside the line, I loop every word by splitting the line in a list of elements separed by a space
        for word in line.split():
            # the first thing that I check is if the word actually contains all vowels (including y)
            if contains_all_vowels(word):
                # if yes, then I check if that vowels appear once and ordered
                if once_and_ordered(word):
                    words_res.append(word)

    print(words_res)
    inf.close()


if __name__ == '__main__':
    main()