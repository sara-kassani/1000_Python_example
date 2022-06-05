# exercise 148: Play Bingo

from dictionaries.ex146 import bingo_cards, display_bingo_cards
from dictionaries.ex147 import winning_card

from random import shuffle
import copy


def play_bingo(card):
    # list of all values between 1 and 75, to be shuffled
    all_values = []
    for i in range(1, 76):
        all_values.append(i)
    shuffle(all_values)

    playcard = copy.deepcopy(card)
    call = 0

    while all_values != []:
        value = all_values.pop()
        call += 1
        for seq in playcard:
            for i in range(5):
                if playcard[seq][i] == value:
                    playcard[seq][i] = 0
                    break
            # if entering another break here, it would not check other seq in case the value is not in the first one
        if winning_card(playcard):
            return call


# BINGO IN DISPLAY MODE
def play_bingo_display_mode(card):
    all_values = []
    for i in range(1, 76):
        all_values.append(i)
    shuffle(all_values)

    playcard = copy.deepcopy(card)
    call = 0
    while all_values != []:
        value = all_values.pop()
        call += 1
        print()
        print('call number %d: the extracted number is %d' % (call, value))
        for seq in playcard:
            for i in range(5):
                if playcard[seq][i] == value:
                    playcard[seq][i] = 0
                    # display_bingo_cards(playcard)
                    break
        if winning_card(playcard):
            print()
            print('you WON at call %d!. Last number called was %d' % (call, value))
            display_bingo_cards(playcard)
            return call


# following function simulates a bingo foor 1000 times on the same card, extracting data
def play_1000_bingo(card):
    # list with all calls that are necessary to end each of the 1000 bingos
    calls = []
    thecard = bingo_cards()
    for i in range(1000):
        call = play_bingo(thecard)
        calls.append(call)
    highest_call = max(calls)
    lowest_call = min(calls)
    avg_call = sum(calls) / 1000
    print('highest call: %d' % highest_call)
    print('lowest call: %d' % lowest_call)
    print('average call: %.1f' % avg_call)


def main():
    # create a card, print it and simulate 1000 times a bingo on the same card
    # this is done to analyze data about max, min and avg call
    mycard = bingo_cards()
    print(mycard)
    play_1000_bingo(mycard)


if __name__ == '__main__':
    main()
