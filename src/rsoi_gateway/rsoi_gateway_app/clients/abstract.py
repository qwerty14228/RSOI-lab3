class AbstractLibraryClient:
    
    def get_libraries(self, city='', page=1, size=10):
        raise NotImplementedError()

    def get_library_books(self, library_uid='', book_uid=None, page=1, size=10, show_all=False): 
        raise NotImplementedError()
    
    def get_library_book(self, library_uid=None, book_uid=None):
        raise NotImplementedError()
    
    def update_book_available_count(self, user=None, library_book_id=None, available_count=0):
        raise NotImplementedError()
    

class AbstractRatingClient:

    def get_rating(self, user=None):
        raise NotImplementedError()
    
    def update_rating(self, user=None, rating_id=None, stars=None):
        raise NotImplementedError()


class AbstractReservationClient:

    def get_reservations(self, user=None, status=None):
        raise NotImplementedError()
    
    def create_reservation(self, user=None, book_uid=None, library_uid=None, till_date=None):
        raise NotImplementedError()
    
    def get_reservation(self, user=None, reservation_uid=None):
        raise NotImplementedError()
    
    def update_reservation(self, user=None, reservation_id=None, status=None):
        raise NotImplementedError()