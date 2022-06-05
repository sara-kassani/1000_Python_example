# exercise 173: Total the Values

def recursive_sum():
    value = input('enter value: ')
    if value == '':
        # HERE IS THE BASE CASE
        return 0
    else:
        return float(value) + recursive_sum()


if __name__ == '__main__':
    print(recursive_sum())
