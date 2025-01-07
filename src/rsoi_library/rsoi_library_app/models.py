from uuid import uuid4

from django.db import models

class Library(models.Model):
    library_uid = models.UUIDField(verbose_name='Library_uid', unique=True, default=uuid4)
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Books(models.Model):
    book_uid = models.UUIDField(verbose_name='Books', unique=True, default=uuid4)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    CONDITIONS = [
        ('EXELLENT', 'EXELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITIONS, default='EXELLENT')
    
class LibraryBooks(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)       
    available_count = models.IntegerField(verbose_name='Availability')