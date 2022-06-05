# exercise 142: Unique Characters

def unique_ch_count(s):
    d = dict()
    count = 0
    for ch in s:
        if ch not in d:
            d[ch] = 1
            count += 1
    return count


# alternative version using a set
def unique_ch_count_bis(s):
    myset = set(s)
    return len(myset)


def main():
    print(unique_ch_count('aaaaabbbcccdefggggghijkkllmmmnnnoopqrsttuvwwwwxxyyyyyyyz'))
    print(unique_ch_count_bis('aaaaabbbcccdefggggghijkkllmmmnnnoopqrsttuvwwwwxxyyyyyyyz'))


if __name__ == '__main__':
    main()
