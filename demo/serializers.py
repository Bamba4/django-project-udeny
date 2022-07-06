from rest_framework import serializers
from .models import Book, BookNumber, Character, Author

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'sur_name']



class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']



class BookSerializer(serializers.ModelSerializer):
    numbers = BookNumberSerializer(many=False)
    characters =  CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id','title', 'description', 'price', 'numbers', 'characters', 'authors']


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title']

