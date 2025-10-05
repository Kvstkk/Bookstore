from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from book_app.models import Book, Author, Publisher
from book_app.serializers import BookDetailSerializer, BookListSerializer, AuthorSerializer, PublisherSerializer


@api_view(['GET'])
def index(request):
    if request.method == "GET":
        return Response(({'a':'a'}))

class BookList(APIView):
    def get(self, request):
        books= Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class BookDetail(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


class AuthorList(APIView):
    def get(self, request):
        authors= Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class PublisherList(APIView):
    def get(self, request):
        publishers= Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)


class PublisherDetail(APIView):
    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        books = Book.objects.filter(publisher=publisher)
        serializer_p = PublisherSerializer(publisher)
        serializer_b = BookListSerializer(books,many=True)
        return Response({
            'publisher': serializer_p.data,
            'books': serializer_b.data
        })

class AuthorDetail(APIView):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        books = Book.objects.filter(author=author)
        serializer_a = AuthorSerializer(author)
        serializer_b = BookListSerializer(books,many=True)
        return Response({
            'author': serializer_a.data,
            'books': serializer_b.data
        })