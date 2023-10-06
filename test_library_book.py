from library_book import LibraryBook, Library

def test_borrow_and_return_books():
    library = Library()
    book1 = LibraryBook("Sample Book 1", "Author 1")
    book2 = LibraryBook("Sample Book 2", "Author 2")
    library.add_book(book1)
    library.add_book(book2)

    # Test borrowing a book
    assert library.borrow_book("Sample Book 1") is True
    assert library.borrow_book("Non-existent Book") is False

    # Test returning a book
    assert library.return_book("Sample Book 1") is True
    assert library.return_book("Sample Book 1") is False

def test_search_books():
    library = Library()
    book1 = LibraryBook("Sample Book 1", "Author 1")
    book2 = LibraryBook("Sample Book 2", "Author 2")
    library.add_book(book1)
    library.add_book(book2)

    # Test searching books
    assert len(library.search_by_title("Sample Book 1")) == 1
    assert len(library.search_by_author("Author 2")) == 1
    assert len(library.search_by_title("Non-existent Book")) == 0
