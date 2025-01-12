from uuid import uuid4

from django.test import TestCase

from rsoi_library_app.models import Library, Books, LibraryBooks

class LibraryTestCase(TestCase):
    library_uid = uuid4()
    
    def setUp(self):
        Library.objects.create(library_uid=self.library_uid, name="Library", city="Moscow", address="Pushkina 7")

    def test_library_read(self):
        library = Library.objects.get(library_uid=self.library_uid)
        self.assertEqual(library.city, "Moscow")
        self.assertEqual(library.address, "Pushkina 7")
        self.assertEqual(library.name, "Library")

    def test_library_creation(self):
        library_uid=uuid4()
        library = Library.objects.create(library_uid=library_uid, name="Library 2", city="SPB", address="Volkova 14")
        self.assertEqual(library.library_uid, library_uid)
        self.assertEqual(library.name, "Library 2")
        self.assertEqual(library.city, "SPB")
        self.assertEqual(library.address, "Volkova 14")

    def test_library_update(self):
        Library.objects.filter(library_uid=self.library_uid).update(address="Pushkina 10")
        library = Library.objects.get(library_uid=self.library_uid)
        self.assertEqual(library.address, "Pushkina 10")

    def test_library_deletion(self):
        Library.objects.filter(library_uid=self.library_uid).delete()
        self.assertEqual(Library.objects.filter(library_uid=self.library_uid).count(), 0)



class BooksTestCase(TestCase):
    book_uid = uuid4()

    def setUp(self):
        Books.objects.create(book_uid=self.book_uid, name="Godunov", author="Pushkin", genre="classic", condition="EXELLENT")

    def test_books_read(self):
        books = Books.objects.get(book_uid=self.book_uid)
        self.assertEqual(books.name, "Godunov")
        self.assertEqual(books.author, "Pushkin")
        self.assertEqual(books.genre, "classic")
        self.assertEqual(books.condition, "EXELLENT")

    def test_books_creation(self):
        book_uid=uuid4()
        books = Books.objects.create(book_uid=book_uid, name="Onegin", author="Pushkin", genre="classic", condition="EXELLENT")
        self.assertEqual(books.book_uid, book_uid)
        self.assertEqual(books.name, "Onegin")
        self.assertEqual(books.author, "Pushkin")
        self.assertEqual(books.genre, "classic")
        self.assertEqual(books.condition, "EXELLENT")

    def test_books_update(self):
        Books.objects.filter(book_uid=self.book_uid).update(condition="GOOD")
        books = Books.objects.get(book_uid=self.book_uid)
        self.assertEqual(books.condition, "GOOD")

    def test_books_deletion(self):
        Books.objects.filter(book_uid=self.book_uid).delete()
        self.assertEqual(Books.objects.filter(book_uid=self.book_uid).count(), 0)


class LibraryBooksTestCase(TestCase):
    library_uid = uuid4()
    book_uid = uuid4()
    lb_id = None

    def setUp(self):
        library = Library.objects.create(library_uid=self.library_uid, name="Library", city="Moscow", address="Pushkina 7")
        book = Books.objects.create(book_uid=self.book_uid, name="Godunov", author="Pushkin", genre="classic", condition="EXELLENT")
        lb = LibraryBooks.objects.create(book=book, library=library, available_count=10)
        self.lb_id=lb.id

    def test_library_books_read(self):
        lb = LibraryBooks.objects.get(id=self.lb_id)
        self.assertEqual(lb.book.book_uid, self.book_uid)
        self.assertEqual(lb.library.library_uid, self.library_uid)
        self.assertEqual(lb.available_count, 10)

    def test_library_books_creation(self):
        book_uid=uuid4()
        book = Books.objects.create(book_uid=book_uid, name="Onegin", author="Pushkin", genre="classic", condition="EXELLENT")
        library=Library.objects.get(library_uid=self.library_uid)
        lb = LibraryBooks.objects.create(book=book, library=library, available_count=15)
        self.assertEqual(lb.book.book_uid, book_uid)
        self.assertEqual(lb.library.library_uid, self.library_uid)
        self.assertEqual(lb.available_count, 15)

    def test_library_books_update(self):
        LibraryBooks.objects.filter(id=self.lb_id).update(available_count=9)
        lb = LibraryBooks.objects.get(id=self.lb_id)
        self.assertEqual(lb.available_count, 9)

    def test_books_deletion(self):
        LibraryBooks.objects.filter(id=self.lb_id).delete()
        self.assertEqual(LibraryBooks.objects.filter(id=self.lb_id).count(), 0)


