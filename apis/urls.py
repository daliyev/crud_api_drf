from django.urls import path

from .views import BookAPIList


urlpatterns = [
    path('', BookAPIList.as_view(), name="book_list"),
]
