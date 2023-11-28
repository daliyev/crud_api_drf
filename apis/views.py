from rest_framework import generics
from mydrf1.models import Book
from .serializers import BookSerializer, UserSerializer

from django.contrib.auth.models import User
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
