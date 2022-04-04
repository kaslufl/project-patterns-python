from .user import User
from .library import Library

class LibraryProxy:
    """class to act as middleman"""
    library: Library

    def list_books(self, user: User) -> list:
        if user.borrowed_books > 0:
            return 'Return your borrowed books before getting more!'
        self.library = Library()
        return self.library.list_books()
