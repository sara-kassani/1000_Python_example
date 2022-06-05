# exercise 121: Random Lottery Numbers

import random


def ticket_generator():
    numbers = []
    while len(numbers) < 6:
        random_n = random.randint(1, 49)
        if random_n not in numbers:
            numbers.append(random_n)
    return sorted(numbers)


def play_lottery(ticket):
    numbers = ticket_generator()
    print('lottery ticket >>>',numbers)
    if numbers == ticket:
        print('You Won :D')
        return True
    if numbers != ticket:
        print('You Lost :(')
        return False


def main():
      my_ticket = ticket_generator()
      print('here is my ticket >>> {}'.format(my_ticket))
      play_lottery(my_ticket)


if __name__ == '__main__':
    main()


""" alternative VERSION of the lottery: game stops as soon as a number not included in the ticket gets extracted
def play_lottery(ticket):
    for i in range(6):
        n = random.randint(1, 49)
        print(n)
        if n not in ticket:
            result = 'you lost'
            return print(result)
"""
