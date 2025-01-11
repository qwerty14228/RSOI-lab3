from uuid import uuid4

from django.db import models

class Reservation(models.Model):
    reservation_uid = models.UUIDField(verbose_name='Reservation_uid', unique=True, default=uuid4)
    username = models.CharField(max_length=80)
    book_uid = models.UUIDField(verbose_name='Book_uid')
    library_uid = models.UUIDField(verbose_name='Library_uid')

    STATUSES = [
        ('RENTED', 'RENTED'),
        ('RETURNED', 'RETURNED'),
        ('EXPIRED', 'EXPIRED'),
        ('CANCELED', 'CANCELED'),
    ]
    status = models.CharField(max_length=20, choices=STATUSES)
    start_date = models.DateField()
    till_date = models.DateField()