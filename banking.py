class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"[{self.user_id}] {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    # Add book
    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully.")

    # Show all books
    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            print(book)

    # Register user
    def add_user(self, user):
        self.users[user.user_id] = user
        print("User registered successfully.")

    # Issue book
    def issue_book(self, book_id, user_id):
        if book_id not in self.books:
            print("Book not found.")
            return
        if user_id not in self.users:
            print("User not found.")
            return

        book = self.books[book_id]
        user = self.users[user_id]

        if book.is_issued:
            print("Book already issued.")
        else:
            book.is_issued = True
            user.borrowed_books.append(book)
            print(f"Book '{book.title}' issued to {user.name}.")

    # Return book
    def return_book(self, book_id, user_id):
        if book_id not in self.books or user_id not in self.users:
            print("Invalid book or user.")
            return

        book = self.books[book_id]
        user = self.users[user_id]

        if book in user.borrowed_books:
            book.is_issued = False
            user.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned.")
        else:
            print("This user didn't borrow this book.")


# ------------------ MAIN PROGRAM ------------------

def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Add User")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            library.add_user(User(user_id, name))

        elif choice == "4":
            book_id = input("Enter Book ID: ")
            user_id = input("Enter User ID: ")
            library.issue_book(book_id, user_id)

        elif choice == "5":
            book_id = input("Enter Book ID: ")
            user_id = input("Enter User ID: ")
            library.return_book(book_id, user_id)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()