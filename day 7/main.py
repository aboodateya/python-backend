class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book added: {book.title} by {book.author}")

    def display_books(self):
        print(f"\n📚 Books in {self.name}:")
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"📖 You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"❌ '{book.title}' is already checked out.")
                    return
        print(f"❌ Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"🔁 You have returned '{book.title}'.")
                    return
                else:
                    print(f"⚠️ '{book.title}' was not checked out.")
                    return
        print(f"❌ Book '{title}' not found in the library.")

def main():
 
    library = Library("City Library")

    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))

  
    library.display_books()

    library.lend_book("1984")
    library.lend_book("To Kill a Mockingbird")

    library.lend_book("1984")

    library.display_books()

    library.return_book("1984")

    library.return_book("The Great Gatsby")

    library.display_books()


if __name__ == "__main__":
    main()
