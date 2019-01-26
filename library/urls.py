from django.urls import path,include
from . import views

urlpatterns = [
    path('add_book',views.add_book,name="Add book"),
    path('search',views.search, name = "Search Books")
]
