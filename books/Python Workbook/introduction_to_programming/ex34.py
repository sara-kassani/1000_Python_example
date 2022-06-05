# exercise 34: Day Old Bread

unit_of_old_bread = int(input('enter number of bought pieces: '))
unit_price = 3.49
discount_rate = 0.60


regular_price = unit_of_old_bread * unit_price
tot_discount = regular_price * discount_rate
final_price = regular_price - tot_discount

print("regular price: %5.2f" % regular_price)
print("discount:      %5.2f" % tot_discount)
print("final price:   %5.2f" % final_price)

""" NOTA: 
%5.2f makes sure the value will take up exactly 5 spaces, 2 of which for decimals, 1 for the dot and 2 
for the integers. This is useful to keep a column in line when the number of digits that are present in prices
and discounts is variable.
"""

"""
print("%d pezzi di pane verrebbero a costare %.2f $, ma applicando lo sconto unitario del 60 percento su ogni pezzo,\
il costo finale è di %.2f $, per uno sconto totale di %.2f $."\
% (unit_of_old_bread, regular_price, final_price, tot_discount))
"""
