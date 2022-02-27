# Module 6 Instance Attributes
class Book:
    language = 'ENG'
    is_book = True

    def set_title(self, value):
        if not isinstance(value, str):
            raise TypeError("The value of the title attribute must be of str type.")
        self.title= value

book= Book()
book.set_title('Python OOP exercises')

print(book.title)

print("{:^12}".format("*****"*10))