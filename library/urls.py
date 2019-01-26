from django.urls import path,include
from . import views

urlpatterns = [
    path('add_book',views.add_book,name="Add book"),
    path('search',views.search, name = "Search Books"),
    path('<int:b_id>',views.book_info, name = "show book info"),
    path('assign',views.assign_book,name = "assign book"),
    path('return',views.mark_returned,name = "marked retruned")
]
