# exercise 87: Shipping Calculator

def shipping_cost(n):
    if n < 1:
        return 'items must be at least 1'
    one_item_shipping = 10.95
    more_items_shipping = 2.95
    tot_shipping_cost = one_item_shipping + (n - 1) * more_items_shipping
    return 'shipping will cost € %.2f' % tot_shipping_cost


def main():
    items = int(input('enter number of purchased items: '))
    print(shipping_cost(items))


if __name__ == '__main__':
    main()
