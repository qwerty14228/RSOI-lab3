from django.test import TestCase

from rsoi_rating_app.models import Rating

class RatingTestCase(TestCase):
    def setUp(self):
        rating = Rating.objects.create(username="test-user", stars=50)
        rating.stars = 75
        rating.save()

    def test_rating_read(self):
        rating = Rating.objects.get(username="test-user")
        self.assertEqual(rating.stars, 75)
        self.assertEqual(rating.username, "test-user")

    def test_rating_creation(self):
        rating = Rating.objects.create(username="test-user2", stars=50)
        self.assertEqual(rating.username, "test-user2")
        self.assertEqual(rating.stars, 50)

    def test_rating_update(self):
        Rating.objects.filter(username="test-user").update(stars=75)
        rating = Rating.objects.get(username="test-user")
        self.assertEqual(rating.stars, 75)

    def test_rating_deletion(self):
        Rating.objects.filter(username="test-user").delete()
        self.assertEqual(Rating.objects.filter(username="test-user").count(), 0)
