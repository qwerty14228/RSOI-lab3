from django.test import TestCase

from rsoi_gateway_app.clients import MockLibraryClient, MockRatingClient, MockReservationClient

class LibraryClientTestCase(TestCase):

    def setUp(self):
        self.client = MockLibraryClient()

    def test_get_libraries(self):
        data = self.client.get_libraries()
        self.assertIsNotNone(data)
        self.assertEqual(1, data['page'])
        self.assertEqual(10, data['pageSize'])
        self.assertLessEqual(len(data['items']), 10)
        self.assertGreaterEqual(data['totalElements'], 0)
        for item in data['items']:
            self.assertIn('libraryUid', item)
            self.assertIn('city', item)
            self.assertIn('name', item)
            self.assertIn('address', item)

    def test_get_library_books(self):
        data = self.client.get_library_books()
        self.assertIsNotNone(data)
        self.assertEqual(1, data['page'])
        self.assertEqual(10, data['pageSize'])
        self.assertLessEqual(len(data['items']), 10)
        self.assertGreaterEqual(data['totalElements'], 0)
        for item in data['items']:
            self.assertIn('bookUid', item)
            self.assertIn('name', item)
            self.assertIn('author', item)
            self.assertIn('genre', item)
            self.assertIn('condition', item)
            self.assertIn('availableCount', item)

    def test_get_library_book(self):
        data = self.client.get_library_book()
        self.assertIsNotNone(data)
        self.assertIn('book', data)
        self.assertIn('library', data)
        self.assertIn('book_uid', data['book'])
        self.assertIn('name', data['book'])
        self.assertIn('author', data['book'])
        self.assertIn('genre', data['book'])
        self.assertIn('condition', data['book'])
        self.assertIn('library_uid', data['library'])
        self.assertIn('city', data['library'])
        self.assertIn('name', data['library'])
        self.assertIn('address', data['library'])
        self.assertIn('available_count', data)

    def test_update_book_available_count(self):
        data = self.client.update_book_available_count()
        self.assertIsNotNone(data)
        self.assertIn('book', data)
        self.assertIn('library', data)
        self.assertIn('book_uid', data['book'])
        self.assertIn('name', data['book'])
        self.assertIn('author', data['book'])
        self.assertIn('genre', data['book'])
        self.assertIn('condition', data['book'])
        self.assertIn('library_uid', data['library'])
        self.assertIn('city', data['library'])
        self.assertIn('name', data['library'])
        self.assertIn('address', data['library'])
        self.assertIn('available_count', data)

class RatingClientTestCase(TestCase):

    def setUp(self):
        self.client = MockRatingClient()

    def test_get_rating(self):
        data = self.client.get_rating()
        self.assertIsNotNone(data)
        self.assertIn('username', data)
        self.assertIn('stars', data)

    def test_update_rating(self):
        data = self.client.update_rating()
        self.assertIsNotNone(data)
        self.assertIn('username', data)
        self.assertIn('stars', data)

    
# class ReservationsTestCase(TestCase):

#     def setUp(self):
#         self.client = 
