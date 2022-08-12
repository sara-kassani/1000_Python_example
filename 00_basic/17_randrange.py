# Rolling dice - randrange
import random
def main():
    # mu= 1, sigma= 6
    print(1 + int(6 * random.random() ))   # 4
    print(random.randrange(1, 7))          # 3

if __name__ == '__main__':
    main()
