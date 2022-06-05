# exercise 112: Remove Outliers

def remove_outliers(li, n):
    t = li.copy()
    t.sort()
    # loop lasts n times
    for i in range(n):
        # removing the first element (index 0) at each iteration
        t.remove(t[0])
        j = len(t)-1
        # removing last element at the same time
        t.remove(t[j])
        j -= 1
    return t


def main():
    mylist = []
    s = input('enter a value (blank to quit): ')
    while s != '':
        mylist.append(float(s))
        s = input('enter a value (blank to quit): ')

    if len(mylist) < 4:
        return print('not enough values')
    else:
        print('with removed outliers >>> {}'.format(remove_outliers(mylist, 3)))
        print('original list: {}'.format(mylist))


if __name__ == "__main__":
    main()
