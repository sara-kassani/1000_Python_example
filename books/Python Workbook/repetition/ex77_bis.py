# exercise 77: Multiplication Table

def mol_table():
    print('', end='\t')
    for i in range(1, 11):
        print(i, end='\t')

    print()

    for i in range(1, 11):
        print(i, end='\t')
        for j in range(1, 11):
            print( i *j, end='\t')
        print()


if __name__ == '__main__':
    mol_table()