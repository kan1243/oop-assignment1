class Book:
    def __init__(self, id, title, author, total_cp, available_cp):
        self.id = id
        self.title = title
        self.author = author
        self.total_cp = total_cp
        self.available_cp = available_cp
        


    def show_avaliable():
        pass


class Library:
    def __init__(self):
        self.book = []
        self.member = []


    def add_book(self, book_id, title, author, available_copies):
        book = Book(book_id, title, author, available_copies, available_copies)
        self.book.append(book)