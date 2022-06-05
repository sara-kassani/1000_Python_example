# exercise 184: Flatten a List

def flatten(data):
    # BASE CASE
    if data == []:
        return data

    if type(data[0]) == list:
        l1 = flatten(data[0])
        l2 = flatten(data[1:])
        return l1 + l2
    else:
        l1 = [data[0]]
        l2 = flatten(data[1:])
        return l1 + l2


if __name__ == '__main__':
    data = [1, [2, 3], [4, [5, [6, 7]]], [[[8, 9], 10]]]
    print(flatten(data))
    data_bis = ['a', 'b', 'c', [{'a': 1}, ('cat', 'dog')], '3', ['4', ('e', 'f', '5', ['g'])]]
    print(flatten(data_bis))
