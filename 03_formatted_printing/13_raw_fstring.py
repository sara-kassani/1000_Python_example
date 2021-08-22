"""
raw f-string
"""
def main():
    name = 'foo'
    print(r"a\nb {name}")
    print(rf"a\nb {name}")
    print(fr"a\nb {name}")          # this is better (for vim)


if __name__ == '__main__' :
    main()