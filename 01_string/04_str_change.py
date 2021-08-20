"""
change a string
"""
def main():
    text = 'abcd'
    print(text)

    text = text[:2] + 'Y' + text[3:]
    print(text)




if __name__ == '__main__':
    main()