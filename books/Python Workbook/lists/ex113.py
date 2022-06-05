# exercise 113: Avoiding Duplicates

word_list = []
word = input('enter word (blank to quit): ')

while word != '':
    if word not in word_list:
        word_list.append(word)
    word = input('enter word (blank to quit): ')

for element in word_list:
    print(element)
