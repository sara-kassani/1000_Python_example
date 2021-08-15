# converting string to int

def main():
    a = '23'
    print(a)
    print(type(a))
    
    b = int(a)
    print(b)
    print(type(b))
    
    a = "30 for life"
    print(a)
    print(type(a))
    
# Error
    b = int(a)
    print(a)
    print(type(b))
    
if __name__ == '__main__':
    main()