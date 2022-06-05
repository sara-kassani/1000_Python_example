# exercise 125: Shuffling a Deck of Cards

import random

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']


def createDeck():
    deck = []
    for v in values:
        for s in suits:
            deck.append(v + s)
    return deck


def shuffle(deck):
    for i in range(0, len(deck)):  # looping each element of the deck
        # searching a random index between 0 and the max index of the deck
        other_pos = random.randrange(0, len(deck))
        # assigning to swap the value of the looped element
        swap = deck[i]
        # substituting the looped element with the element at the random index
        deck[i] = deck[other_pos]
        # lastly assigning to the element at the random index the original value of the looped element
        deck[other_pos] = swap
    return deck


# checking if each card appears maximum once. In case of repetitions, it returns False
def check_deck(d):
    di = dict()
    for c in d:
        if c not in di:
            di[c] = 1
        else:
            return False
    return True


def main():
    mydeck = createDeck()
    print('ordered deck:')
    print(mydeck)
    print()
    mydeck_shuffle = shuffle(mydeck)
    print('shuffled deck:')
    print(mydeck_shuffle)
    print()
    print('the deck has no repetitions:')
    print('>>>', check_deck(mydeck_shuffle))
    # if creating a new sorted Deck, it will always be True: no card repetitions
    #print(check_deck(createDeck()))


if __name__ == '__main__':
    main()
