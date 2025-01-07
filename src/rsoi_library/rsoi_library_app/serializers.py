from rest_framework import serializers

from rsoi_library_app.models import Library, Books, LibraryBooks


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'library_uid', 'name', 'city', 'address']

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'book_uid', 'name', 'author', 'genre', 'condition']

class LibraryBooksSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(write_only=True)
    library_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = LibraryBooks
        fields = ['id', 'book_id', 'library_id', 'book', 'library', 'available_count']
        read_only_fields = ['book', 'library']
        depth = 1
    
    def create(self, validated_data):
        book_id = validated_data.pop('book_id')
        library_id = validated_data.pop('library_id')
        library_books = LibraryBooks.objects.create(book_id=book_id, library_id=library_id, **validated_data)
        return library_books