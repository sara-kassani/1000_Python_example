# exercise 123: Pig Latin Improved

string = input('enter text: ')
res = ''
vowels = ['a', 'e', 'i', 'o', 'u']
punctuation = [',', '.', '?', '!']
punct = ''

i = len(string)-1
# the main of this first loop is to check whether the word ends with punctuation (one or more) or not
for c in string:
    while string[i] in punctuation:  # checking in reverse mode
        # adding each punctuation character until finding, in reverse, a letter,
        punct += string[i]
        i -= 1

# I will do the pig latin conversion on a length which is same as the length of the string with no final punctuation
mylength = len(string) - len(punct)

# if the first letter is a vowel, the conversion is easy: just adding way
if string[0].lower() in vowels:
    final = 'way'
    res = string + final
# if the first letter is a consonant, I check how many consecutive consonant
else:
    final = ''
    initial = ''
    for i in range(mylength):
        if string[i].lower() not in vowels:
            # moving to the end all consonant making them lowercase
            final += string[i].lower()
        # as soon as I find a vowel, I distinguish two similar cases, based on if the first letter is lower or upper
        else:
            # if the original first letter was upper, the new string in pig latin will become as upper
            if string[0].isupper():
                # pushing in initial the remaining substring
                initial = string[i].upper() + string[i+1:mylength]
            else:
                # same logic, counting as lowercase the first letter
                initial = string[i] + string[i+1:mylength]
            break
    res = initial + final + 'ay' + punct

print(res)

# note: punct will store the original ending punctuation but reversed
