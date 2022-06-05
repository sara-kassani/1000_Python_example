# exercise 126: Dealing Hands of Cards

from lists.ex125 import createDeck, shuffle, check_deck


def deal(n_hands, n_cards, deck):
    res = []
    # creating as many sublists as the amount of players
    for hand in range(0, n_hands):
        res.append(list())

    # using a nested loop but firstly made upon cards and then upon players because I will give one card at a time
    # loop lasts as many times as the amount of cards to give each player: first card, second card, etc.
    for c in range(n_cards):
        # the nested loop will last as many times as the amount of players: first card to first player,
        # first card to second player, etc.
        for h in range(n_hands):
            # the dealer will give a card which (extracted from the deck) tp the player 0, then to player 1, and so on
            res[h].append(deck.pop())
    print(res)


def main():
    # print('ordered deck:')
    mydeck = createDeck()
    # print(mydeck)
    # print()

    mydeck_shuffle = shuffle(mydeck)
    print(mydeck_shuffle)
    print('the deck has %d cards in total' % len(mydeck_shuffle))
    # print(check_deck(mydeck_shuffle))
    print()

    print('here are the hands:')
    # parameters choice
    deal(4, 5, mydeck_shuffle)  # depending on parameters each of the 4 players will have 5 cards
    print('the deck has %d remaining cards' % len(mydeck_shuffle))
    # print(mydeck_shuffle) # I can reprint the deck to check


if __name__ == '__main__':
    main()

""" exercise requests
- return a list of lists. Each list-element of the list will be a series of cards
- cards have to be given once at a time to different players (as in reality), and not all at once to each player
"""