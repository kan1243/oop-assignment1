class Book:
    def __init__(self, id_book:str, title:str, author:str, total_coppies:int, available_coppies:int):
        self.id = id_book
        self.title = title
        self.author = author
        self.total_cp = total_coppies
        self.available_cp = available_coppies
        


    def show_all_avalable_book():
        '''show book that have in library right now'''
        print('\n=== Available Books ===')
        for book in library.book:
            if book.available_cp > 0:
                print(f"{book.title} by {book.author} - {book.available_cp} copies available")



class Member:
    def __init__(self, id_member:str, name:str, email:str, borrowed_books:list = []):
        self.id = id_member
        self.name = name
        self.email = email
        self.borrowed_book = borrowed_books


    def show_given_member_borrowed(self, member_id):
        member = func.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member['name']} ===")
        if not member['borrowed_books']:
            print("No books currently borrowed")
        else:
            for book_id in member['borrowed_books']:
                book = func.find_book(book_id)
                if book:
                    print(f"- {book['title']} by {book['author']}")    


class Library:
    def __init__(self):
        '''Library store book and member in list'''
        self.book = []
        self.member = []


    def add_book(self, book_id, title, author, available_copies):
        """Add a new book to the library"""
        book = Book(book_id, title, author, available_copies, available_copies)
        self.book.append(book)
        print(f'Book {title} added successfully!')


    def add_members(self, member_id, name, email):
        """Register a new library member"""
        member = Member(member_id, name, email)
        self.member.append(member)
        print(f'Member {name} added successfully!')


    def borrow_book(self, member_id, book_id):
        # find book and member
        book = func.find_book(book_id)
        member = func.find_member(member_id)


        if not member:
            print("Error: Member not found!")
            return False


#class store function that (help/used by) other class
class Function:
    def __init__(self):
        pass


    def find_book(self, book_id):
        '''find book by id'''
        for book in library.book:
            if book.id == book_id:
                return book
        return None


    def find_member(self, member_id):
        '''find member by id'''
        for member in library.member:
            if member.id == member_id:
                return member
        return None
    

#create object
library = Library()
func = Function()
