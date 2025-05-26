from rest_framework.serializers import ModelSerializer
from .models import Book, Category, Review

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'title','description', 'author', 'length','price',
            'category', 'created_at',  'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name'
        ]

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',  'book', 'description', 'user', 'created_at','updated_at',
        ]
        read_only_fields = ['user','created_at', 'updated_at']
