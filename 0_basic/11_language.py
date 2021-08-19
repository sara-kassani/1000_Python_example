'''
Exercise: What is this language?
- Ask the user the same of this programming language.
- If they type in Python, welcome them
- If they type is something else, correct them
'''
def main():
    lang = input('Enter the name of this programming language:')
    if lang == 'Python':
        print('Welcome!')
    else:
        print(f'No. It is not "{lang}", it is Python.')

if __name__ == '__main__':
    main()