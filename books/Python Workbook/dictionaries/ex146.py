# exercise 146: Create a Bingo Card

import random

B_list = []
I_list = []
N_list = []
G_list = []
O_list = []

for i in range(1, 16):
    B_list.append(i)
for i in range(16, 31):
    I_list.append(i)
for i in range(31, 46):
    N_list.append(i)
for i in range(46, 61):
    G_list.append(i)
for i in range(61, 76):
    O_list.append(i)


def bingo_cards():
    B = []
    for i in range(5):
        r = random.choice(B_list)
        B.append(r)
        B_list.remove(r)
    I = []
    for i in range(5):
        r = random.choice(I_list)
        I.append(r)
        I_list.remove(r)
    N = []
    for i in range(5):
        r = random.choice(N_list)
        N.append(r)
        N_list.remove(r)
    G = []
    for i in range(5):
        r = random.choice(G_list)
        G.append(r)
        G_list.remove(r)
    O = []
    for i in range(5):
        r = random.choice(O_list)
        O.append(r)
        O_list.remove(r)
    d = {'B': B, 'I': I, 'N': N, 'G': G, 'O': O}
    return d


def display_bingo_cards(cards):
    print('-'*20)
    print("%3s %3s %3s %3s %3s" % ('B', 'I', 'N', 'G', 'O'))
    print('-'*20)
    for i in range(5):
        print('%3d %3d %3d %3d %3d' % (cards['B'][i], cards['I'][i], cards['N'][i], cards['G'][i], cards['O'][i]))


def main():
    mycards = bingo_cards()
    print(mycards)
    display_bingo_cards(mycards)


if __name__ == '__main__':
    main()