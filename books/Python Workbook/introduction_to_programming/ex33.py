# exercise 33: Sort 3 Integers

a = int(input('enter the first value: '))
b = int(input('enter the second value: '))
c = int(input('enter the third value: '))

smallest = min(a, b, c)
biggest = max(a, b, c)
# in order to find the middle value, I add all three values and subtract the two I already found
middle = (a+b+c) - smallest - biggest

print("the numbers in sorted order are: %d, %d, %d" % (smallest, middle, biggest))
