from datetime import datetime as dt

import requests

from rsoi_gateway_app.clients.abstract import *


class LibraryClient(AbstractLibraryClient):
    def __init__(self, api_url):
        self.api_url = api_url
    
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
    
    def update_book_available_count(self, user=None, library_book_id=None, available_count=0):
        response = requests.patch(f'{self.api_url}/library_books/{library_book_id}',
                                data={'available_count': available_count}, headers={'X-User-Name': user.username})
        return response.json()
    

class RatingClient(AbstractRatingClient):
    def __init__(self, api_url):
        self.api_url = api_url

    def get_rating(self, user=None):
        response = requests.get(f'{self.api_url}/ratings', headers={'X-User-Name': user.username}, 
                                params={'username': user.username})
        data = response.json()
        if len(data)==0:
            return None
        return data[0]
    
    def update_rating(self, user=None, rating_id=None, stars=None):
        response = requests.patch(f'{self.api_url}/ratings/{rating_id}', data={'stars': stars}, headers={'X-User-Name': user.username})
        return response.json()


class ReservationClient(AbstractReservationClient):
    def __init__(self, api_url):
        self.api_url = api_url

    def get_reservations(self, user=None, status=None):
        if status is None:
            params = {}
        else:
            params = {'status': status} 
        response = requests.get(f'{self.api_url}/reservations', params=params, headers={'X-User-Name': user.username})
        return response.json()
    
    def create_reservation(self, user=None, book_uid=None, library_uid=None, till_date=None):
        start_date = dt.now()
        response = requests.post(f'{self.api_url}/reservations', data={'book_uid': book_uid, 'library_uid': library_uid, 
                                                                       'till_date': till_date, 'username': user.username, 
                                                                       'status': "RENTED", 'start_date': start_date.strftime('%Y-%m-%d')}, headers={'X-User-Name': user.username})
        return response.json()
    
    def get_reservation(self, user=None, reservation_uid=None):
        response = requests.get(f'{self.api_url}/reservations', params={'reservation_uid': reservation_uid}, headers={'X-User-Name': user.username})
        data = response.json()
        if len(data)==0:
            return None
        return data[0]
    
    def update_reservation(self, user=None, reservation_id=None, status=None):
        response = requests.patch(f'{self.api_url}/reservations/{reservation_id}', data={'status': status}, headers={'X-User-Name': user.username})
        return response.json()