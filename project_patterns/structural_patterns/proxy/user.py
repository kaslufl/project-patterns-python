class User:
    """class to represent a library user"""

    borrowed_books: int

    def __init__(self, borrowed_books) -> None:
        self.borrowed_books = borrowed_books
