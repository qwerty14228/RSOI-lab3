from datetime import date

from uuid import uuid4

from django.test import TestCase

from rsoi_reservation_app.models import Reservation

class ReservationTestCase(TestCase):
    reservation_uid = uuid4()
    book_uid = uuid4()
    library_uid = uuid4()

    def setUp(self):
        Reservation.objects.create(
            reservation_uid=self.reservation_uid, username="test-user", 
            book_uid=self.book_uid, library_uid=self.library_uid, 
            status="RENTED", start_date=date(year=2025, month=1, day=1), till_date=date(year=2025, month=2, day=1)
        )

    def test_reservation_read(self):
        reservation = Reservation.objects.get(reservation_uid=self.reservation_uid)
        self.assertEqual(reservation.book_uid, self.book_uid)
        self.assertEqual(reservation.library_uid, self.library_uid)
        self.assertEqual(reservation.status, "RENTED")
        self.assertEqual(reservation.username, "test-user")
        self.assertEqual(reservation.start_date, date(year=2025, month=1, day=1))
        self.assertEqual(reservation.till_date, date(year=2025, month=2, day=1))

    def test_reservation_creation(self):
        reservation_uid = uuid4()
        reservation = Reservation.objects.create(
            reservation_uid=reservation_uid, username="test-user2", 
            book_uid=self.book_uid, library_uid=self.library_uid, 
            status="RETURNED", start_date=date(year=2025, month=1, day=10), till_date=date(year=2025, month=2, day=10)
        )
        self.assertEqual(reservation.book_uid, self.book_uid)
        self.assertEqual(reservation.library_uid, self.library_uid)
        self.assertEqual(reservation.username, "test-user2")
        self.assertEqual(reservation.status, "RETURNED")
        self.assertEqual(reservation.start_date, date(year=2025, month=1, day=10))
        self.assertEqual(reservation.till_date, date(year=2025, month=2, day=10))

    def test_reservation_update(self):
        Reservation.objects.filter(reservation_uid=self.reservation_uid).update(status="EXPIRED")
        reservation = Reservation.objects.get(reservation_uid=self.reservation_uid)
        self.assertEqual(reservation.status, "EXPIRED")

    def test_reservation_deletion(self):
        Reservation.objects.filter(reservation_uid=self.reservation_uid).delete()
        self.assertEqual(Reservation.objects.filter(reservation_uid=self.reservation_uid).count(), 0)
