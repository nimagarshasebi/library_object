

class Book:
    def __init__(self,title,author,year,isbn,status):
        """
        Initializes a new instance of the Book class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
            isbn (str): The ISBN of the book.
            status (str): The status of the book (e.g., 'available', 'borrowed').

        Returns:
            None
        """
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn
        self.status=status
    
    def Borrowing(self,user):
        """
        Changes the status of a book to 'borrowed' when a user borrows it.

        Args:
            user: The user borrowing the book.

        Returns:
            None
        """
        self.status='borrowed'
    def Returning(self):
        """
        Sets the status of a book to 'available' when it is returned.

        Args:
            None

        Returns:
            None
        """
        self.status='available'
    def __str__(self) -> str:
        return f'{self.title} by {self.author} ({self.year})'
    
class User:
    def __init__(self,username,fname,lname,national_code,year_birth,membership_number,role,password):
        """
        Initializes a new instance of the User class.

        Args:
            fname (str): The first name of the user.
            lname (str): The last name of the user.
            national_code (str): The national code of the user.
            year_birth (int): The year of birth of the user.
            membership_number (str): The membership number of the user.

        Returns:
            None
        """
        self.fname=fname
        self.lname=lname
        self.national_code=national_code
        self.year_birth=year_birth
        self.membership_number=membership_number
        self.borrowed_books=[] 
        self.role=role
        self.username=username
        self.password=password
    def borrowing_books(self,book):
        """
        Appends a book to the list of borrowed books.

        Args:
            book: The book to be borrowed.

        Returns:
            None
        """
        self.borrowed_books.append(book)
    def returning_books(self,book):
        """
        Appends a book to the list of borrowed books.

        Args:
            book: The book to be borrowed.

        Returns:
            None
        """
        self.borrowed_books.remove(book)
class Library(Book,User):
    """
        Initializes a new instance of the Library class.

        Args:
            None

        Returns:
            None
    """
    def __init__(self):
        self.books=[]
        self.users=[]

    def add_book(self,book):
        self.books.append(book)

    def add_user(self,user):
        self.users.append(user)
    def remove_book(self,book):
        self.books.remove(book)
    def remove_user(self,user):
        self.users.remove(user)

    def search_by_title(self,title):
        for book in self.books:
            if book.title==title:
                if book.status=='available':
                    return book
                else:
                    return 'The book is borrowed'
            else:
                return 'The book is not found'
        

    def search_by_author(self,author):
        for book in self.books:
            if book.author==author:
                if book.status=='available':
                    return book
                else:
                    return 'The book is borrowed'
            else:
                return 'The book is not found'
              

    def search_by_isbn(self,isbn):
        for book in self.books :
            if book.isbn==isbn:
                if book.status=='available':
                    return book
                else:
                    return 'The book is borrowed'
            else:
                return 'The book is not found'
role=str(input('Enter your role(bookkeeper or customer): '))
library=Library()
while True:
    if role=='admin':
        username=str(input('Enter your username: '))
        for user in library.users:
            if user.username==username:
                passw=str(input('Enter your password: '))
                if user.password==passw:
                    task=str(input('''what do you want to do
                                   (
                                   1-Register person
                                   2-Remove Person
                                   3-Add Book 
                                   4-Remove Book
                                   5-Borrow Book
                                   6-Return Book
                                   )'''))
                    if task=='1':
                        person_username=str(input('Enter your username: '))
                        first_name=str(input('Enter your first name: '))
                        last_name=str(input('Enter your last name: '))
                        national_code=str(input('Enter your national code: '))
                        year_birth=int(input('Enter your year of birth: '))
                        membership_number=str(input('Enter your membership number: '))
                        role=str(input('Enter your role: '))
                        if role=='bookkeeper':
                            password=str(input('Enter your password: '))
                        else:
                            password=None
                        user=User(person_username,first_name,last_name,national_code,year_birth,membership_number,role,password)
                        user_id={'username':person_username,'password':password}
                        library.add_user(user_id)
                    elif task=='2':
                        person_username=str(input('Enter your username: '))
                        library.remove_user(person_username)
                    elif task=='3':
                        title=str(input('Enter the title of the book: '))
                        author=str(input('Enter the author of the book: '))
                        year=int(input('Enter the year of the book: '))
                        isbn=str(input('Enter the ISBN of the book: '))
                        status=str(input('Enter the status of the book: '))
                        book=Book(title,author,year,isbn,status)
                        library.add_book(book)



                    elif task=='4':
                        title=str(input('Enter the title of the book: '))
                        library.remove_book(title)
                    elif task=='5':
                        title=str(input('Enter the title of the book: '))
                        for book in library.books:
                            if book.title==title:
                                user.borrowing_books(book)
                                break
                    elif task=='6':
                        title=str(input('Enter the title of the book: '))
                        for book in library.books:
                            if book.title==title:
                                user.returning_books(book)
                                break
            else:
                continue



