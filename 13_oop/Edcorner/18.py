class Book:
    language= "ENG"
    is_ebook= True

book1 = Book()
book2 = Book()


book1.author= "Dan Brown"
book1.title= "Inferno"

book2.author= "Dan Brown"
book2.title= "The Da Vinci Code"
book2.year_of_publication= 2023

print(book1.__dict__)
print(book2.__dict__)

books= [book1, book2]

for book in books:
    for attr in book.__dict__:
        print(f"{attr} -> {getattr(book, attr)}")
        print("_"*30)


"""
{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publication': 2023}
------------------------------------------------------------------------------------
author -> Dan Brown
______________________________
title -> Inferno
______________________________
author -> Dan Brown
______________________________
title -> The Da Vinci Code
______________________________
year_of_publication -> 2023
______________________________


"""