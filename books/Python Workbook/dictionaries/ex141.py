# exercise 141: Write out Numbers in English

one_to_nineteen = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                   'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                   'nineteen']

twenty_to_ninety = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# dictionary with numbers between 0 and 19 as keys, and words as values
d1 = {}
for i in range(20):
    d1[str(i)] = one_to_nineteen[i]
print(d1)

# dictionary with tens between 20 and 90 as keys, and words as values
d2 = {}
j = 0
for i in range(20, 100, 10):
    d2[str(i)] = twenty_to_ninety[j]
    j += 1
print(d2)


def word_num(n):
    s = str(n)

    if n == 0:
        return 'zero'
    elif n < 20:
        res = d1[s]

    elif 20 <= n < 100:
        res = d2[s[0] + '0'] + ' ' + d1[s[1]]

    elif 100 <= n < 1000:
        if s[1] == '0' and s[2] == '0':
            res = d1[s[0]] + ' hundred'
        elif s[1] == '0':
            res = d1[s[0]] + ' hundred ' + word_num(int(s[2]))
        else:
            res = d1[s[0]] + ' hundred ' + word_num(int(s[1:]))

    else:
        return 'error: please enter a number between 0 and 999'

    return res


def main():
    # printing all numbers between 0 and 999 as strings
    for num in range(1000):
        print(word_num(num))

    print()

    # reading an integer between 0 and 999 to convert it in a word
    num = int(input('enter num: '))
    print(word_num(num))


if __name__ == '__main__':
    main()
