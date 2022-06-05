# exercise 122: Pig Latin

string = input('enter text: ')
res = ''
vowels = ['a', 'e', 'i', 'o', 'u']

if string[0] in vowels:
    final = 'way'
    res = string + final
else:
    final = ''
    initial = ''

    for i in range(len(string)-1):

        if string[i] not in vowels:
            final += string[i]
        else:
            initial += string[i:]
            break
    res = initial + final + 'ay'


print(res)
