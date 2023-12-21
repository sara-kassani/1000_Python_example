class Book:
    language="ENG"
    is_ebbok= True

books_data=[
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {'author': 'Dan Brown', 'title': 'The Davinci COde', 'year_of_publication': '2003'}
    ]

books= []
for book_data in books_data:
    book=Book()

    for attr,value in book_data.items():
        setattr(book, attr, value)

    books.append(book)

for book in books:
    print(book.__dict__)


"""
{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title': 'The Davinci COde', 'year_of_publication': '2003'}
"""