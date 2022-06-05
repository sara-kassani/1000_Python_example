# exercise 6: Tax and Tip

gross = float(input('Price of the meal in euro: '))
VAT = 0.10 * gross
net = gross - VAT
tip = 0.18 * net
print('Price of the meal is €%.2f, €%.2f of which are VAT and €%.2f are tip' % (gross, VAT, tip))


