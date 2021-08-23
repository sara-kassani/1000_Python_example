"""
Anything can be a list
"""
def main():
    lst = [
        42,
        3.14,
        True,
        None,
        'Foo Bar',
        ['another', 'list'],
        {
            'a': 'Dictionary',
            'language': 'Python',
        },
    ]
    print(lst)


if __name__ == '__main__':
    main()