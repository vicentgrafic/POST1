from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer  # serializador
from .models import Author, Book  # modelo de datos


class AuthorViewSet(viewsets.ModelViewSet):
    # ordena todos los objetos ordenados por el campo "name"
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    # ordena todos los objetos ordenados por el campo "name"
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
