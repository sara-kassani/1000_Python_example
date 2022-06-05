# exercise 127: Is a List Already in Sorted Order?

n = input('enter a number: ')
t = []
while n != '':
    t.append(int(n))
    n = input('enter a number (blank to quit): ')

def isSorted(li):
    return li == sorted(li)


print(isSorted(t))


""" DIFFERENCE between sorted() and .sort()
- sorted() takes a list as parameter and returns a new list, sorted, without changing the passed list
- .sort() is a method which is called on a list and sort it, changing it without a return value
"""
