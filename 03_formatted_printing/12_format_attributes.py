"""
Examples using format with attributes of objects
"""
def main():
    import sys
    print("{0.executable}".format(sys))
    print("{system.argv[0]}".format(system = sys))


if __name__ == '__main__':
    main()
