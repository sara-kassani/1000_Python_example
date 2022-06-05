# exercise 108: Reduce Measures

""" info
1 cup = 16 tablespoons
1 tablespoon = 3 teaspoons
t cup = 48 teaspoons
"""


def recipe_instr(units, measure):
    cups = 0
    tablespoons = 0
    teaspoons = 0

    if measure == 'cups':
        cups = units

    if measure == 'tablespoons':
        cups = units // 16
        tablespoons = units % 16

    if measure == 'teaspoons':
        cups = units // 48
        rem_teaspoons = units % 48
        tablespoons = rem_teaspoons // 3
        teaspoons = rem_teaspoons % 3

    # adding to this variable the measure units that are higher than zero distinguishing between singular and plural
    res = ''
    if cups > 0:  # adding to the result only if it is more than zero
        # if more than zero, if units are more than 1, I add the 's' of the plural
        if cups > 1:
            res += '%d cups' % cups
        else:
            res += '%d cup' % cups
    if tablespoons > 0:
        if tablespoons > 1:
            res += ', %d tablespoons' % tablespoons
        else:
            res += ', %d tablespoon' % tablespoons
    if teaspoons > 0:
        if teaspoons > 1:
            res += ', %d teaspoons' % teaspoons
        else:
            res += ', %d teaspoon' % teaspoons

    return res


if __name__ == '__main__':
    print(recipe_instr(59, 'teaspoons'))
