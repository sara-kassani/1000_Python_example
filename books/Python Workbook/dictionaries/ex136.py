# exercise 136: Reverse Lookup

def reverseLookup(d, v):
    list_of_keys = []
    for k in d:
        if d[k] == v:
            list_of_keys.append(k)
    return list_of_keys


def main():
    # creating a dictionary which maps name to age
    name_to_age = {'Bob': 25, 'Jim': 37, 'Alan': 56, 'Kate': 26,\
                   'Lara': 48, 'Jean': 34, 'Jane': 56, 'Joe': 26, 'Jess': 56}
    # returned list will indicate the persons of a specific age
    age = int(input('enter age: '))
    print(reverseLookup(name_to_age, age))


if __name__ == '__main__':
    main()