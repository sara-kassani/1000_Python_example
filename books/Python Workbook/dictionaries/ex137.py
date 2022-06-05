# exercise 137: Two Dice Simulation

import random


def dice_roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    res = dice1 + dice2
    return res


# print(dice_roll())

# dictionary will have potential totals as keys and frequences of that totals as values
d = dict()

# 1000 iterations and adding frequencies of totals in the dictionary
for i in range(1000):
    roll = dice_roll()
    if roll not in d:
        d[roll] = 1
    else:
        d[roll] += 1

# creating a dictionary of frequencies in % starting from created dictionary
d_simulated_percent = dict()
# looping to populate the dictionary of % freq
for k in d:
    freq_percent = (d[k] / 1000) * 100
    d_simulated_percent[k] = float('%.2f' % freq_percent)

# creating a dictionary with expected frequencies of totals, based on probability theory
# potential events / total events ?
d_expected = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36,
              11: 2 / 36, 12: 1 / 36}
# creating again a dictionary of frequencies in %
d_expected_percent = dict()
# looping again as before
for k in d_expected:
    freq_percent = d_expected[k] * 100
    d_expected_percent[k] = float('%.2f' % freq_percent)


def main():
    print(d)  # original dictionary, frequencies as integers
    print()
    print(d_simulated_percent)  # dictionary of simulated frequencies in %
    print()
    print(d_expected_percent)  # dictionary of expected frequencies in %

    print('Total | Sim. % | Exp. %')

    # loops that prints a table Totals - Simulated Frequencies % - Expected Frequencies %
    for i in range(2, 13):
        # the separator aligns table
        print('%5s %7d %7d ' % (i, d_simulated_percent[i], d_expected_percent[i]))


if __name__ == '__main__':
    main()
