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
        self.borrowed_books = borrowed_books


    def show_given_member_borrowed(self, member_id):
        member = func.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = func.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")


class Library:
    def __init__(self):
        '''Library store book and member in list'''
        self.books = []
        self.members = []


    def add_book(self, book_id, title, author, available_copies):
        """Add a new book to the library"""
        book = Book(book_id, title, author, available_copies, available_copies)
        self.books.append(book)
        print(f'Book {title} added successfully!')


    def add_members(self, member_id, name, email):
        """Register a new library member"""
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f'Member {name} added successfully!')


    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        book = func.find_book(book_id)
        member = func.find_member(member_id)

        if not member:
            print("Error: Member not found!")
            return False

        if not book:
            print("Error: Book not found!")
            return False
    
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False

        if len(member.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        book.available_cp -= 1
        member.borrowed_books.append(book_id)

        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member.name,
            'book_title': book.title
        }
        member.borrowed_books.append(transaction)

        print(f"{member.name} borrowed '{book.title}'")
        return True
        

    def return_book(member_id, book_id):
        """Process a book return transaction"""
        member = func.find_member(member_id)
        book = func.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        # Process the return
        book.available_cp += 1
        member.borrowed_books.remove(book_id)

        # Remove from borrowed_books list
        for i, transaction in enumerate(member.borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                member.borrowed_books.pop(i)
                break
            
        print(f"{member.name} returned '{book.title}'")
        return True
    

    def display_operation(self):
        '''display all data in library'''
        print("--- All books in library ---")
        for i in range(len(self.books)):
            book = self.books[i]
            print(f"{i+1}. {book.title}(id: {book.id}, author: {book.author}) {book.total_cp}/{book.available_cp}")

        print("--- All members in library ---")
        for j in range(len(self.members)):
            member = self.members[j]
            print(f"{j+1}. {member.name}(id: {member.id})")

        print(f"Total books: {len(self.books)}")
        print(f"Total members: {len(self.members)}")


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
