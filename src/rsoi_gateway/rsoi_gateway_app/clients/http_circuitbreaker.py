from datetime import datetime as dt

from circuitbreaker import circuit

import requests

from rsoi_gateway_app.clients.http import (
    LibraryClient as BaseHttpLibraryClient,
    RatingClient as BaseHttpRatingClient,
    ReservationClient as BaseHttpReservationClient
)


def get_rating_fallback(self, user=None):
    return {'stars': 50}


def get_libraries_fallback(self, city='', page=1, size=10):
    return {"page": page, "pageSize": size, "totalElements": 0, "items": []}


def get_library_books_fallback(self, library_uid='', book_uid=None, page=1, size=10, show_all=False):
    return {"page": page, "pageSize": size, "totalElements": 0, "items": []}


def get_library_book_fallback(self, library_uid=None, book_uid=None):
    return {
        "book": {
            "book_uid": book_uid,
        },
        "library": {
            "library_uid": library_uid,
        },
        "available_count": 0
    }


def get_reservations_fallback(self, user=None, status=None):
    return []


def get_reservation_fallback(self, user=None, reservation_uid=None):
    return {
        "username": user.username,
        "reservation_uid": reservation_uid
    }


class LibraryClient(BaseHttpLibraryClient):
    @circuit(fallback_function=get_libraries_fallback)
    def get_libraries(self, city='', page=1, size=10):
        return super().get_libraries(city=city, page=page, size=size)

    @circuit(fallback_function=get_library_books_fallback)
    def get_library_books(self, library_uid='', book_uid=None, page=1, size=10, show_all=False): 
        return super().get_library_books(library_uid=library_uid, book_uid=book_uid, page=page, size=size, show_all=show_all)

    @circuit(fallback_function=get_library_book_fallback)
    def get_library_book(self, library_uid=None, book_uid=None):
        return super().get_library_book(library_uid=library_uid, book_uid=book_uid)


class RatingClient(BaseHttpRatingClient):
    @circuit(fallback_function=get_rating_fallback)
    def get_rating(self, user=None):
        return super().get_rating(user=user)


class ReservationClient(BaseHttpReservationClient):
    @circuit(fallback_function=get_reservations_fallback)
    def get_reservations(self, user=None, status=None):
        return super().get_reservations(user=user, status=status)

    @circuit(fallback_function=get_reservation_fallback)
    def get_reservation(self, user=None, reservation_uid=None):
        return super().get_reservation(user=user, reservation_uid=reservation_uid)

    