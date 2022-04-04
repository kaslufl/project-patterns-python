class Library:
    """class to represent a virtual library"""

    books: list[str]

    def __init__(self) -> None:
        self.books = ['One Piece 1', 'Naruto 23', 'Yu Yu Hakusho 3']

    def list_books(self) -> list:
        return self.books
