class Member:
    def __init__(self, name):
        self.name = name
        self.loaned_books = []

    def loan_book(self, book):
        book.loaner = self
        self.loaned_books.append(book)

    def __str__(self) -> str:
        return self.name

class Book:
    def __init__(self, title):
        self.title = title
        self.loaner = None
    
    def return_book(self):
        if not self.loaner is None:
            self.loaner.loaned_books.remove(self)
            self.loaner = None

    def __str__(self) -> str:
        return self.title

class EBook(Book):
    def __init__(self, title, size_mb):
        super().__init__(title)
        self.size_mb = size_mb

donald = Member("Donald")
gatsby = Book("The Great Gatsby")
sapiens = Book("Sapiens: A Brief History of Humankind")

print(gatsby.loaner)
donald.loan_book(gatsby)
print(gatsby.loaner)

digifort = EBook("Digital Fortress", 2.1)
print(digifort.size_mb)


class Newspaper(Book):
    def __init__(self,title, date):
        super().__init__(title)
        self.date = date


newspaper = Newspaper("The New York Times", "12.12.24")
donald = Member("Donald")
print(newspaper.loaner)
donald.loan_book(newspaper)
print(newspaper.loaner)







