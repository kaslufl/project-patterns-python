from project_patterns import LibraryProxy, User


def test_user_with_no_books_borrowed():
    user = User(0)
    library_proxy = LibraryProxy()
    assert(library_proxy.list_books(user) == ['One Piece 1', 'Naruto 23', 'Yu Yu Hakusho 3'])

def test_user_with_books_borrowed():
    user = User(2)
    library_proxy = LibraryProxy()
    assert(library_proxy.list_books(user) == 'Return your borrowed books before getting more!')