# exercise 32: Sum of the Digits in an Integer

value = int(input('enter integer of four digits: '))

value_str = str(value)
sum_of_digits = int(value_str[0]) + int(value_str[1]) + int(value_str[2]) + int(value_str[3])
print(sum_of_digits)


