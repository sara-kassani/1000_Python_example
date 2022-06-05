# exercise 147: Checking for a Winning Card

from dictionaries.ex146 import display_bingo_cards

# vertical
card1 = {'B': [2, 14, 6, 7, 15], 'I': [0, 0, 0, 0, 0], 'N': [43, 44, 41, 33, 45], 'G': [48, 60, 53, 49, 57], 'O': [72, 65, 61, 67, 71]}
# horizontal
card2 = {'B': [2, 14, 0, 7, 15], 'I': [23, 20, 0, 22, 21],
         'N': [43, 44, 0, 33, 45], 'G': [48, 60, 0, 49, 57], 'O': [72, 65, 0, 67, 71]}
# diagonal
card3 = {'B': [0, 14, 6, 7, 15], 'I': [23, 0, 24, 22, 21],
         'N': [43, 44, 0, 33, 45], 'G': [48, 60, 53, 0, 57], 'O': [72, 65, 61, 67, 0]}
# diagonal
card4 = {'B': [2, 14, 6, 7, 0], 'I': [23, 20, 24, 0, 21],
         'N': [43, 44, 0, 33, 45], 'G': [48, 0, 53, 49, 57], 'O': [0, 65, 61, 67, 71]}

# not winning card
bad_card = {'B': [2, 0, 0, 0, 0], 'I': [0, 20, 0, 0, 0],
            'N': [0, 0, 0, 33, 0], 'G': [0, 0, 53, 0, 0], 'O': [72, 0, 0, 0, 71]}


def winning_card(card):
    # VERTICAL check
    for seq in card:
        if not any(card[seq]):
            return True
        # any returns True if even one of the elements of the sequence is True, otherwise it returns False
        # thus, if sequence has all zeroes, it will return False --> winning Card, True from the function

    # HORIZONTAL check
    for i in range(5):
        num_of_zeroes = 0
        for seq in card:
            if card[seq][i] == 0:
                num_of_zeroes += 1
            else:
                # as soon as for the same index I encounter an element of a card different from zero, exit nested loop
                break
        # once a nested loop ends, if number of encountered zeroes is 5, then I have an horizontal line of only zeroes
        if num_of_zeroes == 5:
            return True

    # DIAGONAL check
    i = 0
    num_of_zeroes = 0
    for seq in card:
        if card[seq][i] == 0:
            num_of_zeroes += 1
            i += 1
        else:
            break
    if num_of_zeroes == 5:
        return True

    i = 4
    num_of_zeroes = 0
    for seq in card:
        if card[seq][i] == 0:
            num_of_zeroes += 1
            i -= 1
        else:
            break
    if num_of_zeroes == 5:
        return True

    # if I got here, it means I did not find any zeroes winning combination
    return False


def main():
    # displaying one of the winning cards
    display_bingo_cards(card4)
    print(winning_card(card4))

    # displaying a NOT winning card
    display_bingo_cards(bad_card)
    print(winning_card(bad_card))


if __name__ == '__main__':
    main()