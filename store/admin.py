from itertools import count

from django.contrib import admin
from social_core.pipeline import user

from .models import Book, Category, Review
# Register your models here.




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','price', 'length','category', 'created_at', 'length_message']
    search_fields = ['title', 'author']
    list_editable = ['price']
    autocomplete_fields = ['category']
    list_filter = ['category','created_at', 'updated_at']
    list_per_page = 10


    @admin.display(ordering='length')
    def length_message(self, obj):
        if obj.length < 100:
            return 'short read'
        elif 100 < obj.length < 500:
            return 'decent length'
        else:
            return 'long read'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book','description','user','created_at','updated_at']





