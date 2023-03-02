from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer

from .models import Book
# Create your views here
@api_view(['GET'])
def bibleOverview(request):
    book_urls = {
        'List': '/book-list/',
        'Detail View': '/book-detail/<str:pk>/',
        'Create': '/book-create/',
        'Update': '/book-update/<str:pk>/',
        'Delete': '/book-delete/<str:pk>/',
    }

    return Response(book_urls)

@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)

    if serializer.data.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def bookList(request):
    books = Book.objects.all().order_by('-id')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookDetail(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=requests.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response('Item seccsesfuly delete!')