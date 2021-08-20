"""
string slice (instead of substr)
"""
def main():
    txt = 'hello world!'
    b = txt[1:4]
    print(b)

    print(txt[2:])
    print(txt[:2])

    start = 1
    end = 4
    print(txt[start:end])

if __name__ == '__main__':
    main()