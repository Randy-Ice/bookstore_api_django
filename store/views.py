from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#* sorting, filtering and pagination
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

#* end
# Create your views here.
from .models import Book, Category, Review
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import BookSerializer, CategorySerializer, ReviewSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend ,SearchFilter, OrderingFilter]
    pagination_class = PageNumberPagination
    search_fields = ['title__istartswith','author']
    ordering_fields = ['length', 'created_at']
    filterset_fields = ['title', 'author']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
