# Check if a string can be converted to a number
# isdecimal: Decimal numbers (digits) (not floating point)
# isnumeric: Numeric in the Unicode set (but not floating point number)

def main():
    val = input( "Type a number: " )
    print(val)
    print((val.isdecimal()))
    print(val.isnumeric())

if __name__ == '__main__':
    main()
