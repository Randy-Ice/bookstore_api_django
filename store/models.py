import uuid
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, help_text='Enter a title for the book',
                             validators=[MinLengthValidator(3,
                                        message='title of book should be 3 characters or longer')]
                             )
    description = models.TextField()
    author = models.CharField(max_length=100)
    length = models.IntegerField(
        help_text="Enter the amount of pages this book has to offer",

    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # book_cover_image = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, help_text='Enter a name for the category',
                            validators=[MinLengthValidator(3,
                                        message='name of category should be 3 characters or longer')]
                            )
    def __str__(self):
        return self.name

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    description = models.TextField(help_text='Enter a description for the review',)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'user: {self.user.username} review {self.description[:25]}...'