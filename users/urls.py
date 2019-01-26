from django.urls import path,include
from . import views

urlpatterns = [
    path('login',views.user_login,name= "User Login"),
    path('logout',views.user_logout, name = "User Logout"),
    path('signup',views.user_signup,name="User Sign up ")
]
