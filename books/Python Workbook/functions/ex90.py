# exercise 90: The Twelve Days of Christmas

from ex89 import my_ordinal


def display_verse(n):
    print('On the', my_ordinal(n),
          'day of Christmas')  # my_ordinal(n) prints first, second, third.... based on passed number
    print('my true love sent to me:')
    # if n >= 12 then all below conditions are also True
    if n >= 12:
        print("Twelve drummers drumming")
    # if n >= 11 then all below conditions are True but not the one aboce
    if n >= 11:
        print("Eleven pipers piping")
    # and so on
    if n >= 10:
        print("Ten lords a-leaping")
    if n >= 9:
        print("Nine ladies dancing")
    if n >= 8:
        print("Eight maids a-milking")
    if n >= 7:
        print("Seven swans a-swimming")
    if n >= 6:
        print("Six geese a-laying")
    if n >= 5:
        print("Five golden (gold) rings")
    if n >= 4:
        print("Four calling (colly) birds")
    if n >= 3:
        print("Three french hens")
    if n >= 2:
        print("Two turtle doves")
    # only in case n is 1, the below specific string is printed
    if n == 1:
        print("A partridge in a pear tree")
    # in any other case the below string will be the last line
    else:
        print("And a partridge in a pear tree")
    # using a separation line between strophes for when I will print all strophes one after another
    print()


def main():
    for i in range(1, 13):
        display_verse(i)


if __name__ == '__main__':
    main()
