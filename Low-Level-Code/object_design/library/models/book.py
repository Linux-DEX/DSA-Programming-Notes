class Book:
    def __init__(self, isbn, title, copies):
        if copies < 0:
            raise ValueError("copies must be >= 0")
        self.isbn = isbn
        self.title = title
        self.copies = copies
