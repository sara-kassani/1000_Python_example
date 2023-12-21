"""
Implement a method called set_title() that allows you to set an instance attribute called title. 
Then create an instance of the Book class named book and set the title attribute to ' inferno' 
using the set_title( ) method.
"""

class Book:
    language = "ENG"
    is_ebook = True

    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError("The value of title attribute must be str type.")
        self.title = value
    
book= Book()
try: 
    book.set_title("Python Programming")
except TypeError as error:
    print(error)
    
print(book.title)

"""
Python Programming
"""