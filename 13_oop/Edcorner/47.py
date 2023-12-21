import uuid

class Book:
    def __init__(self, title, author):
        self.book_id=self.get_id()
        self.title=title
        self.author=author

    def __repr__(self):
        return f"Book(title={self.tilte}, author={self.author})"
    
    def __str__(self):
        return f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author}"
    
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])
    

book=Book("Python OOp", "John Doe")
print(book)

"""Book ID: 140659856690647 | Title: Python OOp | Author: John Doe"""