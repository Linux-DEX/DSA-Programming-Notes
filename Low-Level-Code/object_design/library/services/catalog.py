class Catalog:
    def __init__(self):
        self._books = {}

    def add(self, book):
        self._books[book.isbn] = book

    def get(self, isbn):
        return self._books[isbn]
