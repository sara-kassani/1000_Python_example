# exercise 63: Average

total = 0
n = 0
average = 0
while True:
    value = float(input('enter value: '))
    # if value is zero, I make a distinction based on if it was the first value or not
    if value == 0:
        # if average is not zero, then zero was not the first value, thus I print the average
        if average:
            print(average)
        # if average did not get any value it means zero was the first value, thus I print error
        else:
            print('first value cannot be zero')
        # anyway the loop will end when input is zero
        break
    # the numerator grows by the value at each loop
    total += value
    # the denominator grows by 1 at each loop
    n += 1
    average = total / n
