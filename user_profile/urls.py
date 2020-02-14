from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home_page'),
    path('register/', register_new_users, name='register_page'),
    path('login/', login_user, name='login_page'),
    path('logout/', logout_user, name='logout_user'),
    path('change_password/', change_password, name='change_password'),
    path('edit_profile/', edit_profile, name='user_profile'),
]
