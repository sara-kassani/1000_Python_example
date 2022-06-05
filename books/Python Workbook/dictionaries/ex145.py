# exercise 145: Scrabble Score

letters = ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U', 'D', 'G', 'B', 'C',
           'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

points = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 8, 8, 10, 10]

scrabble_d = dict(zip(letters, points))
print(scrabble_d)


def main():
    score = 0
    word = input('enter a word: ')
    for c in word.upper():
        if c in letters:
            score += scrabble_d[c]
    print(score)


if __name__ == '__main__':
    main()
