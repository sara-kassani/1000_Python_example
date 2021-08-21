"""
iterable, iterator
"""
def main():
    # for in loop with early end using break
    txt = 'hello world'
    for ch in txt:
        if ch == ' ':
            break
        print(ch)
    print('Here')

    # for in loop skipping parts using continue
    txt = 'hello world'
    for ch in txt:
        if ch == ' ':
            continue
        print(ch)

    # for in loop with break and continue
    txt = 'hello world'
    for ch in txt:
        if ch == ' ':
            continue
        if ch == 'r':
            break
        print('DONE')
        

if __name__ == '__main__':
    main()