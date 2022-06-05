# exercise 64: Discount Table

discount_rate = 0.60

purchase = 4.95
while purchase <= 24.95:
    discount = purchase * discount_rate
    print('original price: %.2f $' % purchase)
    print('discount: %.2f $' % (purchase * discount_rate))
    print('final price: %.2f $' % (purchase - discount))
    print()
    purchase += 5
