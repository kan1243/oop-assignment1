class Book:
    def __init__(self, id_book:str, title:str, author:str, total_coppies:int, available_coppies:int):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.total_cp = total_coppies
        self.available_cp = available_coppies
        

    def borrow_book(self):
        if self.available_cp > 0:
            self.available_cp -= 1
            return True
        else:
            return False


    def return_book(self):
        self.available_cp += 1


class Member:
    def __init__(self, id_member:str, name:str, email:str):
        self.member_id = id_member
        self.name = name
        self.email = email
        self.borrowed_books = []


    def borrow_book(self, book):
        if book.borrow_book():
            transaction = {
            'member_id': self.member_id,
            'book_id': book.id_book,
            'member_name': self.name,
            'book_title': book.title}
            self.borrowed_books.append(transaction)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print('Error: No copies available!')


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
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        
        if not member:
            print("Error: Member not found!")

        elif not book:
            print("Error: Book not found!")
            
        elif len(member.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        else:
            member.borrow_book(book)
        

    def return_book(self, member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        # Process the return
        book.return_book()
        member.borrowed_books.remove(book_id)

        # Remove from borrowed_books list
        for i, transaction in enumerate(member.borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                member.borrowed_books.pop(i)
                break
            
        print(f"{member.name} returned '{book.title}'")
        return True
    

    def display_operation(self, condition = None, condition_data = None):
        '''display all data in library (uo to condition if no condition mean all)'''
        if condition == 'display_book':
            print("=== Available Books ===")
            for i in range(len(self.books)):
                book = self.books[i]
                if book.available_cp == 0:
                    continue
                else:
                    print(f"-{book.title} by{book.author} - {book.available_cp} copies available")

        if condition == 'display_member':
            member = self.find_member(condition_data)
            if not member:
                print("Error: Member not found!")
                return None

            else:
                print(f"\n=== Books borrowed by {member.name} ===")
                if not member.borrowed_books:
                    print("No books currently borrowed")
                else:
                    for transaction in member.borrowed_books:
                        book = self.find_book(transaction['book_id'])
                        if book:
                            print(f"- {book.title} by {book.author}")


    def find_book(self, book_id):
        '''find book by id'''
        for book in self.books:
            if book.id_book == book_id:
                return book
        return None


    def find_member(self, member_id):
        '''find member by id'''
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    

#create object
library = Library()

def test_library_system():
    """Comprehensive test of all library functions"""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    
    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)
    
    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_members(101, "Alice Smith", "alice@email.com")
    library.add_members(102, "Bob Jones", "bob@email.com")
    library.add_members(103, "Carol White", "carol@email.com")
    
    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_operation('display_book')
    
    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python Crash Course
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python Crash Course
    
    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_operation('display_member', 101)  # Alice's books
    library.display_operation('display_member', 102)  # Bob's books
    library.display_operation('display_member', 103)  # Carol's books (none)
    
    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_operation('display_book')
    
    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    library.display_operation('display_book')
    
    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)  # Bob tries to borrow unavailable book
    
    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)  # Alice's 3rd book
    library.display_operation('display_member', 101)
    library.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)
    
    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)  # Alice returns Python Crash Course
    library.return_book(102, 1)  # Bob returns Python Crash Course
    library.display_operation('display_member', 101)
    library.display_operation('display_book')
    
    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)  # Bob tries to return book he didn't borrow
    
    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)  # Carol returns Pragmatic Programmer
    library.borrow_book(102, 3)  # Bob borrows it
    library.display_operation('display_member', 102)
    
    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)  # Non-existent member
    library.borrow_book(101, 999)  # Non-existent book
    library.return_book(999, 1)  # Non-existent member
    library.display_operation('display_member', 999)  # Non-existent member
    
    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in borrowed_books:
        print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
    
    print("\nAll Members and Their Books:")
    for member in members:
        print(f"\n{member['name']} ({member['id']}):")
        if member['borrowed_books']:
            for book_id in member['borrowed_books']:
                book = find_book(book_id)
                print(f"  - {book['title']}")
        else:
            print("  (No books borrowed)")
    
    library.display_operation('display_book')
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

# Run the comprehensive test
if __name__ == "__main__":
    test_library_system()