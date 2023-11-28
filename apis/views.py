from rest_framework import generics

from mydrf1.models import Book
from .serializers import BookSerializer


class BookAPIList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer