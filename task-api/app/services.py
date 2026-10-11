"""In-memory business logic for books.

Replace this module with a database-backed repository when required.
"""

BOOKS = {}
_NEXT_ID = 1


def list_books():
    """Return all books ordered by ID."""
    return [BOOKS[key].copy() for key in sorted(BOOKS)]


def get_book(book_id):
    """Return a book or None when it does not exist."""
    book = BOOKS.get(book_id)
    return book.copy() if book else None


def create_book(data):
    """Create a book and assign its ID on the server."""
    global _NEXT_ID

    book = {
        "id": _NEXT_ID,
        "title": data["title"].strip(),
        "author": data["author"].strip(),
        "published_year": data["published_year"],
    }
    BOOKS[_NEXT_ID] = book
    _NEXT_ID += 1
    return book.copy()


def update_book(book_id, data):
    """Replace editable fields of an existing book."""
    if book_id not in BOOKS:
        return None

    BOOKS[book_id] = {
        "id": book_id,
        "title": data["title"].strip(),
        "author": data["author"].strip(),
        "published_year": data["published_year"],
    }
    return BOOKS[book_id].copy()


def delete_book(book_id):
    """Delete a book; return True if it existed."""
    return BOOKS.pop(book_id, None) is not None


def reset_books():
    """Reset in-memory state; intended for tests only."""
    global _NEXT_ID
    BOOKS.clear()
    _NEXT_ID = 1
