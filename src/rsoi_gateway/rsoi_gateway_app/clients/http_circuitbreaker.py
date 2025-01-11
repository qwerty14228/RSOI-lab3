from datetime import datetime as dt

from circuitbreaker import circuit

import requests

from rsoi_gateway_app.clients.http import (
    LibraryClient as BaseHttpLibraryClient,
    RatingClient as BaseHttpRatingClient,
    ReservationClient as BaseHttpReservationClient
)


class LibraryClient(BaseHttpLibraryClient):
    def get_libraries(self, city='', page=1, size=10):
        response = requests.get(f'{self.api_url}/libraries', params={"city": city, "page": page, "size": size})
        data = response.json()
        items = data['results']
        for item in items: 
            item['libraryUid'] = item['library_uid']
            del item['library_uid']
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}

    def get_library_books(self, library_uid='', book_uid=None, page=1, size=10, show_all=False): 
        params = {'library__library_uid': library_uid, 'page': page, 'size': size}
        if not show_all:
            params['available_count__gt'] = 0
        if book_uid is not None:
            params['book__book_uid'] = book_uid
        response = requests.get(f'{self.api_url}/library_books', params=params)
        data = response.json()
        items = []
        for result in data['results']: 
            item = result['book']
            item['bookUid'] = item['book_uid']
            del item['book_uid']
            item['availableCount'] = result['available_count']
            items.append(item)
        return {"page": page, "pageSize": size, "totalElements": data["count"], "items": items}
    
    def get_library_book(self, library_uid=None, book_uid=None):
        params = {"library__library_uid": library_uid, "book__book_uid": book_uid}
        response = requests.get(f'{self.api_url}/library_books', params=params)
        data = response.json()
        if len(data['results']) == 0:
            return None
        return data['results'][0]
    

def get_rating_fallback(self, user=None):
    return {'stars': 50}


class RatingClient(BaseHttpRatingClient):
    @circuit(fallback_function=get_rating_fallback)
    def get_rating(self, user=None):
        return super().get_rating(user=user)

class ReservationClient(BaseHttpReservationClient):
    def get_reservations(self, user=None, status=None):
        if status is None:
            params = {}
        else:
            params = {'status': status} 
        response = requests.get(f'{self.api_url}/reservations', params=params, headers={'X-User-Name': user.username})
        return response.json()
    
    def get_reservation(self, user=None, reservation_uid=None):
        response = requests.get(f'{self.api_url}/reservations', params={'reservation_uid': reservation_uid}, headers={'X-User-Name': user.username})
        data = response.json()
        if len(data)==0:
            return None
        return data[0]
    