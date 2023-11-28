from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet
from .views import BookViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'book', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', BookAPIList.as_view(), name="book_list"),
]
