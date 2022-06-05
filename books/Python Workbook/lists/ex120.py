# exercise 120: Formatting a List

def formatting_list(li):
    if len(li) == 1:
        print(li[0] + '.')
    else:
        mystring = ''
        for element in li:
            if element == li[-1]:
                mystring += element + '.'
            elif element == li[-2]:
                mystring += element + ' and '
            else:
                mystring += element + ', '
        print(mystring)


def main():
    mylist = ['apples', 'oranges', 'melons', 'lemons']
    formatting_list(mylist)

    element = input('enter element (blank to quit): ')
    el_list = []
    while element != '':
        el_list.append(element)
        element = input('enter element (blank to quit): ')
    print(el_list)
    formatting_list(el_list)


if __name__ == '__main__':
    main()

