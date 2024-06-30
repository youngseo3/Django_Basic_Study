from django.shortcuts import render, redirect
from .forms import BookForm
from myapp.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})
