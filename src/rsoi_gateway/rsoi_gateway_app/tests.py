from django.test import TestCase

from rsoi_gateway_app.clients import MockLibraryClient

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
