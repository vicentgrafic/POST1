from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # modelo de datos que va a serializar/deserializar
        model = Author
        # campos del modelo de datos que va a serializar/deserializar
        fields = ('name', 'created_date')

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # modelo de datos que va a serializar/deserializar
        model = Book
        # campos del modelo de datos que va a serializar/deserializar
        #fields = ('title', 'description', 'author', 'added_by')
        fields = ('title', 'description', 'author')