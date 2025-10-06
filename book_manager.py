class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.get_title()} added to library.")

    def list_books(self):
        for book in self.books:
            print(f"{book.get_title()} by {book.get_author()}")
