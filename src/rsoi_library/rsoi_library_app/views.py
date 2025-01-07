from django.http import HttpResponse
from rest_framework import permissions, viewsets

from rsoi_library_app.models import Library, Books, LibraryBooks
from rsoi_library_app.serializers import LibrarySerializer, BooksSerializer, LibraryBooksSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('library_uid')
    serializer_class = LibrarySerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('city',)

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('book_uid')
    serializer_class = BooksSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]

class LibraryBooksViewSet(viewsets.ModelViewSet):
    queryset = LibraryBooks.objects.all()
    serializer_class = LibraryBooksSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ('available_count', 'library__library_uid', 'book__book_uid')


def healthcheck_view(request):
    
    return HttpResponse("")
