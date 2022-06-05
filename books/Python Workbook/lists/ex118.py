# exercise 118: Word by Word Palindromes

import string


def is_wbw_palindrome(sentence):
    # splitting the sentence based on whitespace
    s_list = sentence.split()

    # converting each element into a lowercase word with no punctuation
    for i in range(len(s_list)):
        word = s_list[i].strip(string.punctuation).lower()
        s_list[i] = word

    # creating a reversed list from the previous list
    s_list_rev = []
    rev_index = len(s_list) - 1
    for i in range(len(s_list)):
        s_list_rev.append(s_list[rev_index])
        rev_index -= 1

    # checking if both the original and reversed list are the same
    if s_list == s_list_rev:
        return True
    else:
        return False


def main():
    mystring = input('please enter a sentence: ')

    if is_wbw_palindrome(mystring):
        print('That\'s a word by word palindrome')
    else:
        print('Not a word by word palindrome')


if __name__ == '__main__':
    main()

