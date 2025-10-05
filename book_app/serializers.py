from rest_framework import serializers
from book_app.models import Book, Publisher, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    publisher = serializers.CharField(source='publisher.name')
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'genre', 'price', 'popularity']


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    publisher = serializers.CharField(source='publisher.name')
    class Meta:
        model = Book
        fields = '__all__'