# exercise 173: Total the Values

value = 0


def fun_sum():
    global value
    new_value = input('enter value: ')

    if new_value == '':
        # HERE IS THE BASE CASE
        return value
    else:
        value += int(new_value)
        return fun_sum()


if __name__ == '__main__':
    print(fun_sum())
