# exercise 76: Multiple Word Palindromes

sentence = input('enter string: ')
# making all lowercase
sentence = sentence.lower()
# it will store only letters without any other type of character
sentence_no_space = ''

for i in range(len(sentence)):
    if 97 <= ord(sentence[i]) <= 122:
        # adding only letters to variable
        sentence_no_space += sentence[i]

print(sentence_no_space)
# here I will create the reverse string in order to compare it with the original
sentence_rev_no_space = ''

j = len(sentence_no_space)-1
while j > -1:
    sentence_rev_no_space += sentence_no_space[j]
    j -= 1

if sentence_rev_no_space == sentence_no_space:
    print('it is a palindrome')
else:
    print('not a palindrome')
