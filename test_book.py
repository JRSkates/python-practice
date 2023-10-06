from book import Book

def test_borrow_book():
  book = Book("Sample Book", "Author Name", 3)
  assert book.borrow_book() is True  # Borrowing the first available copy should return True
  assert book.borrow_book() is True  # Borrowing the second available copy should return True
  assert book.borrow_book() is True  # Borrowing the last available copy should return True
  assert book.borrow_book() is False  # No available copies left, borrowing should return False

def test_return_book():
  book = Book("Sample Book", "Author Name", 2)
  assert book.borrow_book() is True
  assert book.borrow_book() is True
  assert book.borrow_book() is False
  book.return_book()
  assert book.borrow_book() is True