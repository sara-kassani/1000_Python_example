# exercise 84: Coin Flip Simulation

import random


def coin_flip():
    rep_H = 0
    rep_T = 0
    flips = 0
    sequence = ''
    while rep_H < 3 and rep_T < 3:
        side = random.randint(1, 2)
        flips += 1
        if side == 1:
            rep_H += 1
            rep_T = 0
            sequence += ' H'
        elif side == 2:
            rep_T += 1
            rep_H = 0
            sequence += ' T'
        if rep_H == 3 or rep_T == 3:
            print(sequence, '(%d flips)' % flips)
            return flips


num_of_simulations = 10
tot_flips = 0

for i in range(num_of_simulations):
    tot_flips += coin_flip()

average_flips = tot_flips / num_of_simulations
print('on average, %.1f flips were needed in order to encounter three consecutive equal H or T' % average_flips)
