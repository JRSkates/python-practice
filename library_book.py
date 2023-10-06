class LibraryBook:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

class Library:
    def __init__(self):
      self.books = []

    def add_book(self, book):
      self.books.append(book)

    def search_by_title(self, title):
      return [book for book in self.books if book.title.lower() == title.lower()]

    def search_by_author(self, author):
      return [book for book in self.books if book.author.lower() == author.lower()]

    def borrow_book(self, title):
      for book in self.books:
        if book.title.lower() == title.lower() and book.available:
          book.available = False
          return True
      return False

    def return_book(self, title):
      for book in self.books:
        if book.title.lower() == title.lower() and not book.available:
          book.available = True
          return True
      return False
