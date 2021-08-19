"""
Flag
"""
def main():
    correct = False
    name = input('The name of this progeamming language: ')

    if name == 'Python':
        correct = True
    else:
        print(' Incorrect input!')

    if correct:
        print('Correct input.')


if __name__ == '__main__':
    main()