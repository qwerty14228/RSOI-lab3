from rsoi_gateway_app.clients.abstract import *


class MockLibraryClient(AbstractLibraryClient):
    def get_libraries(self, city='', page=1, size=10):
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                    "name": "Библиотека имени 7 Непьющих",
                    "city": "Москва",
                    "address": "2-я Бауманская ул., д.5, стр.1"
                }
            ]
        }
        items = data['results']
        for item in items: 
            item['libraryUid'] = item['library_uid']
            del item['library_uid']
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}

    def get_library_books(self, library_uid='', book_uid=None, page=1, size=10, show_all=False): 
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "book": {
                        "id": 1,
                        "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
                        "name": "Краткий курс C++ в 7 томах",
                        "author": "Бьерн Страуструп",
                        "genre": "Научная фантастика",
                        "condition": "EXCELLENT"
                    },
                    "library": {
                        "id": 1,
                        "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                        "name": "Библиотека имени 7 Непьющих",
                        "city": "Москва",
                        "address": "2-я Бауманская ул., д.5, стр.1"
                    },
                    "available_count": 1
                }
            ]
        }
        items = []
        for result in data['results']: 
            item = result['book']
            item['bookUid'] = item['book_uid']
            del item['book_uid']
            item['availableCount'] = result['available_count']
            items.append(item)
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}
    
    def get_library_book(self, library_uid=None, book_uid=None):
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "book": {
                        "id": 1,
                        "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
                        "name": "Краткий курс C++ в 7 томах",
                        "author": "Бьерн Страуструп",
                        "genre": "Научная фантастика",
                        "condition": "EXCELLENT"
                    },
                    "library": {
                        "id": 1,
                        "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                        "name": "Библиотека имени 7 Непьющих",
                        "city": "Москва",
                        "address": "2-я Бауманская ул., д.5, стр.1"
                    },
                    "available_count": 1
                }
            ]
        }
        if len(data['results']) == 0:
            return None
        return data['results'][0]
    
    def update_book_available_count(self, user=None, library_book_id=None, available_count=0):
        data = {
            "id": 1,
            "book": {
                "id": 1,
                "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
                "name": "Краткий курс C++ в 7 томах",
                "author": "Бьерн Страуструп",
                "genre": "Научная фантастика",
                "condition": "EXCELLENT"
            },
            "library": {
                "id": 1,
                "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                "name": "Библиотека имени 7 Непьющих",
                "city": "Москва",
                "address": "2-я Бауманская ул., д.5, стр.1"
            },
            "available_count": 150
        }
        return data
    
class MockReservationClient(AbstractLibraryClient):
    def get_reservations(self, user=None, status=None):
        data = [
            {
                "id": 1,
                "username": "ivan",
                "reservation_uid": "9e162628-d9e1-463c-9a7e-9873d29a9fde",
                "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
                "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                "status": "RENTED",
                "start_date": "2025-01-08",
                "till_date": "2025-03-08"
            }
        ]
        return data
    
    def create_reservation(self, user=None, book_uid=None, library_uid=None, till_date=None):
        return {
            "id": 1,
            "username": "ivan",
            "reservation_uid": "9e162628-d9e1-463c-9a7e-9873d29a9fde",
            "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
            "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
            "status": "RENTED",
            "start_date": "2025-01-08",
            "till_date": "2025-03-08"
        }
    
    def get_reservation(self, user=None, reservation_uid=None):
        data = [
            {
                "id": 1,
                "username": "ivan",
                "reservation_uid": "9e162628-d9e1-463c-9a7e-9873d29a9fde",
                "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
                "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
                "status": "RENTED",
                "start_date": "2025-01-08",
                "till_date": "2025-03-08"
            }
        ]
        if len(data)==0:
            return None
        return data[0]
    
    def update_reservation(self, user=None, reservation_id=None, status=None):
        return {
            "id": 1,
            "username": "ivan",
            "reservation_uid": "9e162628-d9e1-463c-9a7e-9873d29a9fde",
            "book_uid": "f7cdc58f-2caf-4b15-9727-f89dcc629b27",
            "library_uid": "83575e12-7ce0-48ee-9931-51919ff3c9ee",
            "status": "EXPIRED",
            "start_date": "2025-01-08",
            "till_date": "2025-03-08"
        }
    
class MockRatingClient(AbstractRatingClient):
    def get_rating(self, user=None):
        data = [
            {
                "id": 1,
                "username": "rsoi-user",
                "stars": 50
            }
        ]
        if len(data)==0:
            return None
        return data[0]
    
    def update_rating(self, user=None, rating_id=None, stars=None):
        return {
            "id": 1,
            "username": "rsoi-user",
            "stars": 70
        }