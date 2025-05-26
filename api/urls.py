from django.urls import path
from rest_framework.routers import  DefaultRouter
from store.views import BookViewSet, CategoryViewSet, ReviewViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls
