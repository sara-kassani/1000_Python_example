"""
Format braces, bracket and parentheses
To print { include {{.
To print } include }}.
Anything that is not in curly braces will be formatted as they are.
"""
def main():
    print('{{{}}}'.format(42))              # {42}
    print('{{ {} }}'.format(42))            # { 42 }
    print('[{}] ({})'.format(42, 42))       # [42] (42)
    print('%{}'.format(42))                 # %42


if __name__ == '__main__':
    main()