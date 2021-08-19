"""
Exercise: Number guessing game
- generate a whole number between 1 and 20
"""
import random


def main():
    hidden = random.randrange(1, 21)
    print('The hidden value is: ', hidden)

    user_guess = input('Enter your guess:')
    print(user_guess)

    guess = int(user_guess)

    if guess == hidden:
        print('Hit!')

    elif guess < hidden:
        print('Your guess is too low!')
    else:
        print('Your guess is too high!')


if __name__ == '__main__':
    main()
