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
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'