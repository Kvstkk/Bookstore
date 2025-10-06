from rest_framework import status
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
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookDetailSerializer(book)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorList(APIView):
    def get(self, request):
        authors= Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            books = Book.objects.filter(author=author)
            serializer_a = AuthorSerializer(author)
            serializer_b = BookListSerializer(books,many=True)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({
            'author': serializer_a.data,
            'books': serializer_b.data
        })

    def put(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if Book.objects.filter(author=author).exists():
            return Response({"error": "You cannot delete this author"
                                      "(There are books with this author)"},
                            status=status.HTTP_400_BAD_REQUEST)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherList(APIView):
    def get(self, request):
        publishers= Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherDetail(APIView):
    def get(self, request, pk):
        try:
            publisher = Publisher.objects.get(pk=pk)
            books = Book.objects.filter(publisher=publisher)
            serializer_p = PublisherSerializer(publisher)
            serializer_b = BookListSerializer(books,many=True)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({
            'publisher': serializer_p.data,
            'books': serializer_b.data
        })

    def put(self, request, pk):
        try:
            publisher = Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            publisher = Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if Book.objects.filter(publisher=publisher).exists():
            return Response({"error": "You cannot delete this publisher"
                                      "(There are books with this publisher)"},
                            status=status.HTTP_400_BAD_REQUEST)

        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)