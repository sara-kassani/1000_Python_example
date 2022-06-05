# exercise 9: Compound Interest

init_amount = float(input('here is the initial amount deposited: '))
interests = 0.04
amount_1st = init_amount * 1.04
amount_2nd = amount_1st * 1.04
amount_3rd = amount_2nd * 1.04
print('initial deposit: €%.2f\n1st year savings: €%.2f\n2nd year savings: €%.2f\
\n3rd year savings: €%.2f' % (init_amount, amount_1st, amount_2nd, amount_3rd))


# NOTE: \ character in print statement tells python that the statement continues on next line


# print('the initial deposit of €%.2f'%init_amount,'will become €%.2f'%amount_1st,'\
# at the end of the first year, €%.2f'%amount_2nd,'at the end of the second year, and\
# €%.2f'%amount_3rd,'at the end of the third year.')

