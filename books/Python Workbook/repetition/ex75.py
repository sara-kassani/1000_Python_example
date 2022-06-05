# exercise 75: Is a String Palindrome?

string = input('enter string: ')

string_rev = ''
i = len(string)-1
while i > -1:
    string_rev += string[i]
    i -= 1

if string_rev == string:
    print(string, 'is a palindrome')
else:
    print('not a palindrome')

# check solution of the book which is optimised with True and False conditions without creating the reverse string
