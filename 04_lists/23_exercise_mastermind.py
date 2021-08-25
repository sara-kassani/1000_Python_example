"""
Exercise: MasterMind
Implement the MasterMind game.
        The computer "thinks" a number with 4 different digits.
        You guess which digits. For each digit that matched both in value, and in location the computer gives you a *.
        For every digit that matches in value, but in space the computer gives you a +.
        Try to guess the given number in as few guesses as possible.
"""


def main():
    import random
    width = 4
    USED = '_'

    hidden = random.sample(range(10), width)
    # print(hidden)

    while True:

        inp = input('your guess ({} digits):'.format(width))
        if inp == 'x':
            print('Bye')
            exit()

        if len(inp) != width:
            print('We need exactly {} characters'.format(width))
            continue

        guess = []
        for cr in inp:
            guess.append(int(cr))
            # guess = list(map(int, inp))
            # print(guess)

        if hidden == guess:
            print('Match')
            break

        my_hidden = hidden[:]
        my_guess = guess[:]

        result = ''
        for i in range(width):
            if my_hidden[i] == my_guess[i]:
                result += '*'
                my_hidden[i] = USED
                my_guess[i] = USED

        for i in range(width):
            if my_guess[i] == USED:
                continue
            if my_guess[i] in my_hidden:
                loc = my_hidden.index(my_guess[i])
                my_hidden[loc] = USED
                guess[i] = USED
                result += '+'
        print(''.join(result))


if __name__ == '__main__':
    main()