# exercise 159: Two Word Random Password

import random
import os.path

file_of_words = os.path.join("..", "files", "words.txt")

inf = open(file_of_words, 'r')

all_words = inf.readlines()

password = ''
n = 0

while len(password) < 8 or len(password) > 10 or len(choice1) < 3 or len(choice2) < 3:
    choice1 = random.choice(all_words)
    choice2 = random.choice(all_words)
    password = choice1.capitalize() + choice2.capitalize()
    n += 1
    # in concatenation I will have the new file as \n at the end of each word and I must remove it
    password = password.replace('\n', '')
    print('attempt number %d: %s' % (n, password))
    print(len(password), 'characters')
    print()

print('SAVED password: %s' % password)
