class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


book1 = Book(id_=1, name='Test Book 1', pages=200)
book2 = Book(id_=2, name='Test Book 2', pages=150)

library = Library(books=[book1, book2])

next_book_id = library.get_next_book_id()

new_book = Book(id_=next_book_id, name='Test Book 3', pages=180)

library.books.append(new_book)

book_id_to_find = 2
book_index = library.get_index_by_book_id(book_id_to_find)

if book_index is not None:
    print(library.books[book_index])
